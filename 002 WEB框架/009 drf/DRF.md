##### 1、DRF介绍

- Django-REST-Framework，是一个基于DJango的重量级RESTAPi插件，用于构建webAPi的工具

-  REST，即Representational State Transfer的缩写 ,我们一般叫他'表现层状态转化'。 REST是一种软件架构设计风格, 不是标准, 也不是技术实现, 它只是提供了一组设计原则和约束条件, 是目前最流行的API设计规范, 用于web数据接口的设 计。

  - 基于http和https协议(超文本传输协议)
- URL/URl 统一资源定位符/统一资源标识符，使用名词复数来表示资源
  - 由HTTP协议动词表示对资源的操作方式(GET POST DELETE PUT PATCH)
  - 对资源的操作会引进资源状态的迁移(表征性状态转移)
  - 本质：无状态，水平扩展，
  
- restful架构：

  - 本质：无状态，尽可能幂等性，便于水平扩展

- HTPP协议是无状态的，不保留连接，在两次请求之间HTTP协议本身不会保留任何关于用户的信息。

  - 但对于服务器来说，记住用户又很重要。三种办法：
    HTTP 无状态 和服务器用户跟踪矛盾如何解决：
    1、 URL重写（在URL种携带用户标识）
    2、隐藏表单域（埋点）<input type='hidden' name=>
    3、浏览器本地存储 
    	--cookie --请求头（自动携带当前网站的Cookie）
    	--localStorage(windos对象)，关掉浏览器还会存在
    	--sessionStorage,浏览器关闭就不存在了

- HTTP报文格式：

  - 请求

    ```
    请求行（1行） GET/HTTP/1.1
    请求头（多行） 一些键值对 HOST connection cache-conntrol cookie
    空行
    消息体
    ```

  - 响应

    ```
    响应行 HTTP/1.1 200
    响应头 键值对
    空行
    响应体
    ```

##### 2、DRF中视图函数

- FBV

  - @api_view(["GET","POST","PATCH"])

    def index(request):

    ​	return Response('你好')

- CBV

  ​	继承自 APIView等类

- request :
  - DRF中的request扩充了django中request，把django的request作为了自己的一个私有属性_request
  - 原生的request只能接受POST参数，现在request.DATA可以接受POST,PUT，PATCH参数。
- Response
  - 内容决策器，根据请求头的ACCept进行决策
  - 可以根据不同的客户端，返回不同样式的数据，返回的时候通过Content-type

##### 3.APIView视图类

- ###### APIView(继承自django的view)

  - 重写了as_view方法

    - queryset检测，给予一个懒加载的值
    - 实现csrf_exempt cstf豁免
    - 调用父类的as_view,有参数检测等
    - 调用APIView中的dispath(就近原则)

  - 重写了dispatch方法

    - 调用了intialize_request
      - 使用django的requrst构建了DRF中的Request
    - intial 初始化
      - get_format_suffix  获取格式化后缀
      - perform_content_negotiation 执行内容决策
      - determin_version 版本检测
      - perform_authentication 用户认证
      - check_permissions 权限检查
      - check_throttles 节流检测
- 根据请求方法名字进行分发
      - 存在对应的视图函数 调用开发者代码
      - 没有抛异常
  
    - 在inial和分发过程中有异常，调用handle_exception处理
-  最后返回   finalizer_response(request,response,*args)
   
- ```
    #复数
    class PersonsAPIView(APIView):
        def get(self,request):
            persons = Person.objects.filter()
            serializer = PersonSerializer(persons,many= True)
            data = {'code':200,'data':serializer.data }
            return Response(data)
        def post(self,request):
            serializer = PersonSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                data = {'code':201,'data':serializer.data}
            return Response(data)
    url中 path('persons/',PersonsAPIView.as_view())
    
    #单数
    class PersonAPIView(APIView):
        def get_object(self,id):
            try:
                person =Person.objects.get(pk=id)
                return person
            except Exception as e:
                raise exceptions.NotFound
    #获取对象
        def get(self,request,id):
            person =self.get_object(id)
            serializer = PersonSerializer(person)
            data = {
                'code':200,
                'data':serializer.data
            }
            return Response(data)
    #更新，这里put跟patch一样，因为自己调用的序列化类用了partial =True,可以部分更新，以后用其他view，直接写Serializer_class时，put跟patch有区别
        def put(self,request,id):
            person = self.get_object(id)
            serializer =PersonSerializer(person,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response('更新失败')
        #删除成功
        def delete(self, request, id):
           	person = self.get_object(id)
    
    		person.delete()
    
    		data = {
    		"code": 204
    		}
    
    return Response(data)    
    路由：re_path(r'^person/(?P<id>\d+)/', PersonAPIView.as_view())
    或	path('person/<int:id>/',PersonAPIView.as_view())
    ```

- GenericAPIView(APIView)    

  属性： 主要添加了与模型相关的操作

  ```
  queryset  查询集
  
  serializer_class   序列化类
  
  lookup_field   查询字段默认是pk
  
  lookup_url_kwarg   
  
  filter_backend    过滤字段
  
  pagination_class  分页器类
  
  ```

  方法：对应上面的属性

  ```
  get__queryset()
  
  get_object()  #查询，如果上面lookup_url_kwarg和lookup_field不满足条件，可以重写
  get_object()
  get_serializer（) 
  #它会调用 get_serializer_class()和get_serializer_context
  
  filter_quertset()
  paginator()
  ```

  代码

  ```
  class PersonAPIView(GenericAPIView):
  
      queryset = Person.objects.all()
      serializer_class = PersonSerializer
  
      def get(self, request):
          queryset = self.get_queryset()
          serializer = self.get_serializer(queryset, many=True)
          return Response(serializer.data)
  
      def post(self, request):
  
          serializer = self.get_serializer(data=request.data)
  
          if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
          return Response(serializer.errors)
  ```

  

- CreateAPIView(GenericAPIView,CreateModelMixin)

  - createAPIView实现了post方法，方法中调用了CreateModelMixin 的create方法，create中调用了perform_create方法来保存

    ```
    源代码
    def perform_create(self,serializer):
    	serializer.save()  #如有需要可以重写
    ```

- ListAPIView(GenericAPIView,listModelMixin)

  - ListAPIView实现了get方法,调用了ListModelMixin的list方法。

- UpdateAPIView(GenericAPIView,updateModelMixin)

  - UpdateAPIview实现了put和patch方法，UpdateModelMixin实现了，update和partial_update

    ```
    #源代码
    def update(self,request,*args,**kwargs):
    	partial = kwargs.pop('partial',False)
    	instance = self.get_object()
    	serializer = self.get_serializer(instance,data=request,data,partial = partial)
    	serializer.is_valid(raise_exception=True)
    	self.perform_update(serializer)
    ```

- RetrieveIpdateDestroyAPIView

  代码

  ```
  #多个
  class BlogsAPIView(ListCreateAPIView):
      queryset = Blog.objects.all()
      serializer_class = BlogSerializer
      authentication_classes = xxx,
      permission_classes = xxx,
  
      def perform_create(self, serializer):
          serializer.save(b_author=self.request.user)
  路由:re_path(r'^blogs/', PersonAPIView.as_view()),
  
  #单个
  class PersonAPIView(RetrieveUpdateDestroyAPIView):
      queryset = Person.objects.all()
      serializer_class = PersonSerializer
      authentication_classes = xxx,
      permission_classes = xxx,
      throttle_classes = xxx,
      
  路由:re_path(r'^persons/(?P<pk>\d+)/', PersonAPIView.as_view()),
  ```

  同一个接口实现注册登录

  ```
  class UsersAPIView(CreateAPIView):
  
      queryset = User.objects.all()
      serializer_class = UserSerializer
  
      def post(self, request, *args, **kwargs):
          action = request.query_params.get("action")
  
          if action == "register":
              return self.do_register(request, *args, **kwargs)
          elif action == "login":
              return self.do_login(request, *args, **kwargs)
          else:
              return self.no_action(request, *args, **kwargs)
  
      def do_register(self, request, *args, **kwargs):
          return self.create(request, *args, **kwargs)
  
      def do_login(self,request, *args, **kwargs):
  
          u_name = request.data.get("u_name")
          u_password = request.data.get("u_password")
  
          users = User.objects.filter(u_name=u_name)
  
          if not users.exists():
              raise exceptions.NotFound()
          user = users.first()
  
          if not user.verify_password(u_password):
              raise exceptions.ValidationError(detail="password error")
  
          token = uuid.uuid4().hex
  
          cache.set(token, user, 60*60*24*7)
  
          data = {
              "msg": "ok",
              "status": 200,
              "token": token
          }
  
          return Response(data)
  
      def no_action(self,request, *args, **kwargs):
  
          # print(cache.get("e92300b15aa54aecadce4df398ad9eae"))
  
          raise exceptions.ValidationError(detail="error action")
          
          
    路由：    re_path(r'^users/$', views.UsersAPIView.as_view()),
  
  ```

  

- 等等相互组合，在generics.py文件中

##### 4.viewsets.py 文件中

- ViewSetMixin(object)
  - 属性
    - action
    - basename
    - description
    - detail
    - name
    - suffiix
  - 方法
    - as_view
    - initialize_request
    - reverse_ation
    - get_extra_actions

- ViewSet(ViewSetMixin.APIView)   #自己没实现
- GenericViewSet(ViewSetMixin,GenericAPIView)   #自己也没实现
- ReadOnlyModelViewSet(ListModelMIxin,RetrieveModelMixin,GenericViewSet) #自己也没实现
- modelViewSwt(GenericViewSet,modelMixin全系列)   #自己也没实现

##### 5.权限认证和节流

- APIView  > as_view >dispatch >initial    在这里进行认证、权限节流

- 认证(确定身份)   request.user(property方法，执行身份认证)

  - 内置了一些认证器，遍历认证器，认证成功一个即可

  - 认证成功返回用户和令牌的元组，存在request上，认证失败默认值填充，对执行也无影响

  - 实现自己的认证 

    ```
    class TokenAuthentication(BaseAuthentication):
        def authenticate(self, request):
            token = request.query_params.get("token")
    
            user = cache.get(token)
    
            if user:
                return user, token
                
                
    #在相应的类视图中加入 authentication_classes = TokenAuthentication,
    ```

- 权限

  - 不同用户身份有不同的权限，check_permissions(执行权限检测)

  - 内置了一些权限,

  - 实现自己的认证

    ```
    class UserLoginPermission(BasePermission):
    
        SAFE_METHODS = ["GET", "HEAD", "OPTIONS"]
    
        def has_permission(self, request, view):
            return request.method in self.SAFE_METHODS or isinstance(request.user, User)
    
        def has_object_permission(self, request, view, obj):
            return obj.b_author.id == request.user.id
            
            
    #has_permission是在check_permission 是检测的
    #has_object_permission是在 get_object 时候检测的，(查看一个对象时,对象权限）
    #在相应的视图类中添加permission_classes = UserLoginPermission,
    ```

- 节流

  ```
  class TenPerMinuteThrottle(SimpleRateThrottle):
  
      rate = "10/m"
  
      def get_cache_key(self, request, view):
          return self.get_ident(request)
          
   #在相应的视图类中加入throttle_classes = TenPerMinuteThrottle,       
  ```

6、序列化验证

```
class PerosonSerializer(serializers.ModelSerializer):
	class Meta:
		model =Person
		fields = ['name','age','password']
	def validate_age(self,value):  #对单个字段
		if 0<int(value)< 100:
			return value
		raise serializers.ValidationError('年龄出错')
	def Validata(self,attrs):#对多个字段校验
		#attrs是一个字典，里面是传过来的所有字段
		if xxx:
			return attrs
		else:
			raise serializers.ValidationError('参数有误')
		
    def create(self, validated_data):
        password_hash = make_password(validated_data.get("password"))
        validated_data["password"] = password_hash
        return super().create(validated_data)

    class Meta:
        model = Person
        fields = ['name','password']
        
 class Person(models.Model):
 	xxx = 
 	password =
 	def verify_password(self, password):
        return check_password(password, self.password)
```

restful架构：

1、协议还是基于http和https协议，还是请求响应式协议

2、URL 统一资源定位符，使用名词来表示资源

3、由HTTP协议动词 来表示对资源的操作方式（GET,POST,DELETE,PUT,PATCH）

4、对资源的操作会引起资源状态的迁移（表征性状态转移）

5、本质：无状态、水平扩展

HTPP协议是无状态的，不保留连接，在两次请求之间HTTP协议本身不会保留任何关于用户的信息。

