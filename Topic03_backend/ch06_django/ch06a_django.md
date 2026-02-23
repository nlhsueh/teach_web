###### tags: `Web`

# Ch06 Django Application

## Reference

* [W3school tutorials- Tennis example](https://www.w3schools.com/django/index.php)
* [Nienlin Hsueh 投影片](https://docs.google.com/presentation/d/1N1aFjWdkCn0jMXeHF6Af6xw18bIkG-UjRMDRGVtN0IE/edit?usp=sharing)
* [django docs](https://docs.djangoproject.com/en/5.0/)

## 網球俱樂部 (I)

#### 基礎

常用目錄相關指令 (windows, cmd terminal)
```
// 回到上目錄
cd ..

// 切到子目錄 my_tennis_club
cd my_tennis_club

// 目前路徑
pwd

// 查看檔案
dir
```

版本控制
```
// 把專案複製到你的電腦
git clone https://github.com/nlhsueh/nlh_tennis_club.git

// 檢查一下目前在的分支
git branch

// 切換到 b01 分支
git checkout b01

// 強制切換到 b01 分支，忽略目前的修改
git checkout -f b01

// 強制清除目前所新增的
git clearn -fd
```

### Lab01: 安裝與啟動
:::success
:football: You will learn
* 如何建立一個虛擬的環境來安裝、執行 django
* 如何建立一個 django 的專案
* 如何開啟一個 django 的網頁伺服器
:::

See [w3school- django install](https://www.w3schools.com/django/django_getstarted.php)

以下是精簡指令大全：
```
// 建立虛擬環境
py -m venv myworld

// 啟動虛擬環境
myworld\Scripts\activate.bat

// 安裝 Django
py -m pip install Django

// 建立專案
django-admin startproject my_tennis_club

// 啟動伺服器
py manage.py runserver
```

這時候到 `http://127.0.0.1:8000` 就會看到一個被啟動的系統（一個火箭）。表示安裝成功。

### Lab02: 用 View-Template say Hello
:::success
:football: You will learn
* 使用 django 中的 ulrs, View 和 Template
:::


Reference to [W3School- create App](https://www.w3schools.com/django/django_create_app.php)

1. [建立子系統](#lab2.1-建立子系統)
2. [設計視界回應 (VIEW)](#2-設計視界回應)
3. [設定網址路由](#3-設定網址路由)
    * 專案路由 `urls.py`
    * 子系統路由 `urls.py`
4. [設計頁面樣板 (TEMPLATE)](#4-設計頁面樣板)

#### lab2.1 建立子系統

```
// 建立一個 app (子系統)
py manage.py startapp members
```

到 `my_tennis_club/my_tennis_club/settings.py:
` 加上新的 app：（**注意**：一定要先執行 startapp 後才能改設定）

```python=
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'members'
]
```
第 2-7 行為預設已加入的 app
這些是 Django 預設安裝的應用程式（apps），它們提供了一系列常用的功能和服務，以協助開發 Web 應用程式。讓我來簡述一下每個應用程式的作用：

1. `django.contrib.admin`: 提供一個自動生成管理介面的框架，讓開發者可以輕鬆地管理網站的後台資料，包括用戶、群組、資料庫內容等。
2. `django.contrib.auth`: 提供用戶身份驗證和權限管理的功能，包括用戶登錄、登出、註冊、密碼重置等功能，並且支持多種身份驗證方式。
3. `django.contrib.contenttypes`: 提供了內容類型框架，用於管理和追蹤 Django 模型的內容類型，使得模型之間可以建立通用的關聯關係。
4. `django.contrib.sessions`: 提供用於處理用戶 Session 的框架，使得開發者可以在 Web 應用程式中存儲和管理用戶的 Session 數據，以實現用戶會話跟踪等功能。
5. `django.contrib.messages`: 提供用於在 Web 應用程式中顯示消息的框架，包括成功、錯誤、警告等不同類型的消息，用於向用戶提供操作結果反饋。
6. `django.contrib.staticfiles`: 提供靜態文件處理的功能，包括收集靜態文件、提供靜態文件的 URL、管理靜態文件的版本等，用於管理和服務靜態資源（如 CSS、JavaScript 文件）。


#### lab2.2 設計視界回應

接受到請求 (request) 後，系統的回應會設計在 `views.py` 中。

> my_tennis_club/members/views.py:

```python=
from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello world!")
```

:question: request 物件提供了哪些資訊？透過 print() 列印出來看看吧

```python=
for attr_name in dir(request):
    if not attr_name.startswith('__'):
        attr_value = getattr(request, attr_name)
        print(f"{attr_name}: {attr_value}")
```

#### lab2.3 設定網址路由

* 當我們打 `127.0.0.1:8000/xxx` 時，會透過網址路由來對應到相對的回應模組 (views)
* django 中，網址路由直接由 `urlpatterns` 來設定, 寫在 `urls.py` 中。
* **專案路由** 的 `urlpatterns` 放在專案下，主要設定admin 的路徑和其他子系統的路徑。
* **子系統路由** 設定路徑與回應模組的關係，放在該子系統的 `urls.py` 下。

專案路由：加上第五行的設定

> my_tennis_club/my_tennis_club/urls.py:

```python=
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('members.urls')),
    path('admin/', admin.site.urls),
]
```

子系統路由：

> my_tennis_club/members/urls.py: 

**注意**：此 `urls.py` 須自己建立
```python=
from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='members'),
    path('members/', views.members, name='members'),
]
```

設定好後，重新啟動伺服器 (
`py manage.py runserver`); 開啟 [http://127.0.0.1:8000](http://127.0.0.1:8000) 和 [http://127.0.0.1:8000/members](http://127.0.0.1:8000/members)，應該會看到 Hello World 的字樣。

:question: 把專案路由的預設路徑改為`tennis`, 試試網頁如何輸出？

:question: 在 `urls.py` 中，加上 `print()` 的指令，印出 `urlspatterns` 的內容

#### lab2.4 設計網頁樣板

修改步驟 2 的「設計視界回應」，讓輸出套用網頁樣板
* 生成樣板物件
* 由樣辦物件做回應 (HttpResponse)

> my_tennis_club/members/views.py:

```python=
from django.http import HttpResponse
from django.template import loader

def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())
```

`myfirst.html` 是放在 `my_tennis_club/members/templates/` 下：(**注意**：目錄 `templates` 需要自己建立)

```html
<!DOCTYPE html>
<html>
<body>

<h1>Hello World!</h1>
<p>Welcome to my first Django project!</p>

</body>
</html>
```

### Lab03: 用 MVT 管理與呈現資料

:::success
:football: You will learn
* 如何建立資料庫的資料
    * model 與 makemigrations, migrate
* 如何透過 shell 新增資料
* 如何讀取資料，並將之呈現在網頁中
    * 網頁樣板標籤與樣板變數的意義
:::

這個 lab 中，我們設計一個會員資料庫，並呈現之。

#### 1. Model

* Model 是設計資料的地方，每一個資料表用一個 class 來宣告設計:
    * 必須繼承 `models.Model`
* 每個資料欄位有不同的型態，常見的如
    * 字串 (`CharField`), 
    * 整數 (`IntegerField`), 
    * 日期 (`DateField`),
* 不同型態的資料有不同的參數設定，例如 `Charfield` 需要設定最大長度
* `__str__()` 用來設計該資料被要求顯示時，該如何顯示


```python=
from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.firstname} {self.lastname}" 
```

#### 2. Migration

當我們對資料庫的格式進行了變更，就必須告知系統，有兩步驟：
1. 產生資料遷移檔 (makemigration)
2. 執行遷移 (migrate)

```
python manage.py makemigrations
python manage.py migrate
```

#### 3. 在終端機新增資料

進入終端機，進入 django 的環境：
```
python manage.py shell
```

查看資料

```python=
from members.models import Member
Member.objects.all() # check all members
nick = Member(lastname='Hsueh',
              firstname='Nien-Lin') # new member
nick.save() 
Member.objects.all() # check again
Member.objects.all().values() # check detail values
```
:question: check the type of `Member.objects.all().values()`

:question: 如何在 shell 中直接執行一個 .py 檔來新增一群資料？

```
exec(open('path/to/your/file.py').read())
```

#### 4. 修改視界回應

```python=
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))
```
* `context` 使用 `dict` 的結構封裝參數
* `template` 透過 `.render` 把參數和請求送到網頁 

#### 讀取與呈現資料


```html=
<!DOCTYPE html>
<html>
<body>

<h1>Members</h1>
  
<ul>
  {% for x in mymembers %}
    <li>{{ x.firstname }} {{ x.lastname }}</li>
  {% endfor %}
</ul>

</body>
</html>
```
* 樣板變數 (template variable)
    * `{{ var }}`
* 樣板標籤 (template tag)
    * `{% for %}`, `{% endfor %}`
    * see [all template tag](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/)

See branch **[member](https://github.com/nlhsueh/nlh_tennis_club/tree/member)**

## 網球俱樂部 (II)
### 資料庫限制

在設計資料庫時，為了確保資料的**完整性 (Integrity)** 和**有效性 (Validity)**，我們需要定義各種限制 (Constraints)。這些限制會在資料庫層級強制執行，防止不符合規則的資料被寫入。

以下是一些常見的資料庫限制及其在 Django 模型中的對應方式：

#### 1. 資料類型限制 (Data Type Constraints)

* **定義：** 每個欄位都必須儲存特定類型 (例如：整數、字串、日期等) 的資料。這是最基本的限制。
* **Django 範例：** Django 模型中的每個欄位都必須指定一個 Field 類型，例如 `IntegerField`, `CharField`, `DateField`, `EmailField` 等。

    ```python
    from django.db import models

    class Product(models.Model):
        name = models.CharField(max_length=100)  # 字串類型，限制最大長度
        price = models.DecimalField(max_digits=10, decimal_places=2)  # 十進位類型，限制總位數和小數位數
        quantity = models.IntegerField()  # 整數類型
        is_available = models.BooleanField(default=True)  # 布林類型
        created_at = models.DateTimeField(auto_now_add=True)  # 日期時間類型
    ```

#### 2. 非空限制 (NOT NULL Constraint)

* **定義：** 確保欄位的值不能為 `NULL`。
* **Django 範例：** 在 Django 模型中，預設情況下欄位允許 `NULL` 值。要設定非空限制，需要將 `null` 參數設為 `False`。

    ```python
    class Category(models.Model):
        name = models.CharField(max_length=50, null=False)  # name 欄位不能為 NULL
    ```

##### null 與 blank

`null` 和 `blank` 常常搞混，前者是**資料庫限制**，後者是**表單限制**。基於 `phone = models.CharField(max_length=20, null=False, blank=True)` 對應 TT, TF, FT, FF 四種狀況，說明了 `null` 和 `blank` 的組合及其含義：

|  `null`   |  `blank`  |  狀況  | 含義 (針對 `phone` 欄位)                                                                                                                                                                         |
| :-------: | :-------: | :----: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **True**  | **True**  | **TT** | 資料庫**允許** `NULL` 值。Django 表單**允許**留空字串 (`''`)。電話號碼在資料庫中可以是沒有值 (`NULL`) 的，使用者在表單中也可以不填寫。                                                           |
| **True**  | **False** | **TF** | 資料庫允許 `NULL` 值。Django 表單**不允許**留空字串 (`''`)。電話號碼在資料庫中可以是沒有值 (`NULL`) 的，但是使用者在表單中**必須填寫**，不能留空。                                               |
| **False** | **True**  | **FT** | 資料庫**不允許** `NULL` 值。Django 表單允許留空字串 (`''`)。電話號碼在資料庫中**必須有值** (但可以是空字串 `''`)，使用者在表單中可以不填寫。當表單留空提交時，資料庫會儲存空字串 (`''`)。        |
| **False** | **False** | **FF** | 資料庫**不允許** `NULL` 值。Django 表單**不允許**留空字串 (`''`)。電話號碼在資料庫中**必須有值** (且不能是 `NULL`)，使用者在表單中**必須填寫**，不能留空。這是強制要求使用者提供電話號碼的設定。 |


#### 3. 唯一性限制 (UNIQUE Constraint)

* **定義：** 確保欄位中的所有值都是唯一的。
* **Django 範例：** 使用 `unique=True` 參數可以為欄位增加唯一性限制。

    ```python
    class User(models.Model):
        username = models.CharField(max_length=30, unique=True)  # username 必須是唯一的
        email = models.EmailField(unique=True)  # email 也必須是唯一的
    ```
    也可以在模型層級定義多個欄位的聯合唯一性約束：

    ```python
    class Meta:
        unique_together = (('first_name', 'last_name'),)  # first_name 和 last_name 的組合必須是唯一的
    ```
    或者使用 `UniqueConstraint` (Django 2.2+):

    ```python
    from django.db.models import UniqueConstraint

    class Person(models.Model):
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)

        class Meta:
            constraints = [
                UniqueConstraint(fields=['first_name', 'last_name'], name='unique_full_name')
            ]
    ```

#### 4. 主鍵限制 (PRIMARY KEY Constraint)

* **定義：** 唯一標識資料表中的每一行。每個資料表只能有一個主鍵。主鍵通常是非空且唯一的。
* **Django 範例：** Django 模型預設會自動建立一個名為 `id` 的 `AutoField` 欄位作為主鍵。你可以選擇其他欄位作為主鍵，但通常不建議修改預設行為。

    ```python
    class Book(models.Model):
        book_id = models.AutoField(primary_key=True)  # 明確指定 book_id 為主鍵 (通常不需要)
        title = models.CharField(max_length=200)
    ```

#### 5. 外鍵限制 (FOREIGN KEY Constraint)

* **定義：** 用於建立和強制執行不同資料表之間的關係。外鍵欄位的值必須參考另一個資料表的主鍵。
* **Django 範例：** 使用 `ForeignKey` 欄位來定義外鍵關係。

    ```python
    class Author(models.Model):
        name = models.CharField(max_length=100)

    class Article(models.Model):
        title = models.CharField(max_length=200)
        author = models.ForeignKey(Author, on_delete=models.CASCADE)  # author 是外鍵，參考 Author 模型
    ```
    * `on_delete`: 定義當參考的父物件被刪除時，子物件應該如何處理 (`CASCADE`, `PROTECT`, `SET_NULL`, `SET_DEFAULT`, `DO_NOTHING` 等)。
        * `CASCADE`: author 被刪除，其所關聯的 article 一起被刪除。
        * `PROTECT`: 刪除 author 時，因為已有 book 與之關聯，會跳出警告避免被刪。
        * `SET_NULL`: author 被刪除，Article 相關聯的 author 欄位被設為 null。Article 的 author 必須允許為 null (`null=True`)。
        * `SET_DEFAULT`: author 被刪除時，Article 中的 author 設為預設值(如 `default="unknown"`)。
        * `DO_NOTHING`: author 被刪就被刪，不做任何處理，強烈不建議，會造成資料的不完整。

#### 6. 檢查限制 (CHECK Constraint)

* **定義：** 定義一個布林表達式，用於限制欄位中允許的值。只有滿足表達式的值才能被接受。
* **Django 範例：** Django 模型在早期版本中沒有直接支援 CHECK constraint。從 Django 3.2 開始，可以使用 `CheckConstraint` (Django 3.2+)。

    ```python
    from django.db.models import CheckConstraint, Q

    class Order(models.Model):
        quantity = models.IntegerField()
        status = models.CharField(max_length=20)

        class Meta:
            constraints = [
                CheckConstraint(check=Q(quantity__gt=0), name='quantity_greater_than_zero'),
                CheckConstraint(check=Q(status__in=['pending', 'processing', 'shipped', 'delivered']), name='valid_status')
            ]
    ```

#### 7. 預設值限制 (DEFAULT Constraint)

* **定義：** 為欄位指定一個預設值，當在插入新記錄時沒有提供該欄位的值時，將使用預設值。
* **Django 範例：** 使用 `default` 參數為欄位設定預設值。

    ```python
    class Task(models.Model):
        description = models.TextField()
        is_completed = models.BooleanField(default=False)  # 預設為 False
        priority = models.IntegerField(default=3)  # 預設優先級為 3
    ```

#### 8. 長度限制 (LENGTH Constraint)

* **定義：** 限制字串或二進制資料欄位的最大長度。
* **Django 範例：** `CharField` 和 `TextField` 可以使用 `max_length` 參數來設定最大長度。

    ```python
    class BlogPost(models.Model):
        title = models.CharField(max_length=255)  # 標題最大長度為 255
        content = models.TextField()
    ```

#### 9. 列舉限制 (ENUM Constraint)

* **定義：** 限制欄位只能從預先定義的一組值中選擇。
* **Django 範例：** Django 雖然有 Enum 類型，也常用 `TextChoices` 搭配 `choices` 參數來模擬列舉限制。

    ```python
    class OrderStatus(models.TextChoices):
        PENDING = 'PD', 'Pending'
        PROCESSING = 'PR', 'Processing'
        SHIPPED = 'SH', 'Shipped'
        DELIVERED = 'DE', 'Delivered'

    class Shipment(models.Model):
        status = models.CharField(max_length=2, choices=OrderStatus.choices, default=OrderStatus.PENDING)
    ```

#### 總結

合理地使用資料庫的各種限制對於建立一個健壯、可靠的應用程式至關重要。它們有助於確保資料的準確性、一致性和完整性。Django 的模型定義提供了方便的方式來聲明這些限制，並且 Django 的 ORM 會在與資料庫互動時考慮這些限制。在設計模型時，仔細思考每個欄位的限制，將有助於避免後續的資料問題。

### Lab04: 管理者與欄位設定
:::success
:football: You will learn
* 如何建立一個管理者 (admin) 的帳號和密碼
* 如何修改資料庫的資料表，需要注意哪些設定
* 建立資料表時，額外的參數設定
:::


#### 建立管理者

```
py manage.py createsuperuser
```
* 你可以用 admin 或是取其他的名字，接著設定密碼。
* 建立後就可以到 [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) 操作。
* 在 admin 的管理中加上 members 等模組，如此 admin 才看得到這些資料。See [W3School- admin include models](https://www.w3schools.com/django/django_admin_include_members.php)

```pytho=
from django.contrib import admin
from .models import Member

# Register your models here.
admin.site.register(Member)
```

#### 新的欄位：電話與加入日期

幫每一個會員增加屬性：電話及加入日期，他們的型態分別是整數與日期。
* `IntegerField`
* `DateField`

```python=
class Member(models.Model):
   firstname = models.CharField(max_length=255)
   lastname = models.CharField(max_length=255)
   phone = models.IntegerField()
   joined_date = models.DateField()
```

`DateField` 的生成方法- 透過字串
```python=
from members.models import Member
x = Member.objects.all()[0]
x.phone = 5551234
x.joined_date = '2022-01-05'
x.save()
```

**更新資料庫結構可能產生的問題**：假設資料庫中有六個會員，本來的欄位只有姓名 (firstname, lastname)，現在增加了電話與日期，如果這兩個欄位被設定為「不可空值」，那麼前面的六個會員就會違反資料庫的設定。解決方法：
1. 改為可以 null
2. 設定一個預設值
3. 先改為可以 null, 增加欄位資料後再改回來

:point_right: [See w3school- django update model](https://www.w3schools.com/django/django_update_model.php)

:point_right: [See django doc- more data types](https://docs.djangoproject.com/en/5.0/ref/models/fields/)

#### 資料欄位的延伸設定

```python=
firstname = models.CharField(max_length=255,
                            null=True,
                            blank=True)
```

以下是 Django 中 CharField 常用的參數及其說明的表格整理：

| 參數名稱       | 說明                                                         |
| -------------- | ------------------------------------------------------------ |
| max_length     | 字串的最大長度。                                             |
| blank          | 表示字串是否可以為空值。預設為 False。是表單檢查相關的。     |
| null           | 資料庫中的字串是否可以為空值。預設為 False。是資料庫相關的。 |
| default        | 字串的預設值。                                               |
| choices        | 定義選項的列舉，用於限制可選的值。                           |
| verbose_name   | 字串的人類可讀名稱，用於在管理界面顯示。                     |
| help_text      | 字串的幫助文字，用於在管理界面顯示字串的說明。               |
| primary_key    | 字串是否為資料的主鍵。預設為 False。                         |
| unique         | 表示字串的值是否唯一。預設為 False。                         |
| editable       | 表示字串是否可以在管理界面中編輯。預設為 True。              |
| error_messages | 定義自定義錯誤消息的字典，用於定義錯誤的顯示。               |

:point_right: [See geeksforgeeks- CharField](https://www.geeksforgeeks.org/charfield-django-models/)

:basketball: 在資料庫 model 中，加上 `unique`, `verbose_name`, `help_text`, `error_message` 等參數，觀察在 admin 頁面的變化。 

:question: 說明以下含義：
```python=
phone = models.IntegerField(null=True, 
                            blank=True,
                            verbose_name='電話')
joined_date = models.DateField(null=True,
                               blank=True,
                               verbose_name='入會日期',
                               default=datetime.date.today(),
                               help_text='the day he pay fee',
                               editable=True,
                               )
```

See branch **[admin](https://github.com/nlhsueh/nlh_tennis_club/tree/admin)**

### Lab05: 細節資料與擴充頁面

:::success
:football: You will learn
* 細節資料的頁面設計
* 主頁面與擴充頁面的設計，以提升主頁面設計的可重用性，將地程式開發的複雜度。
:::

<概述資料-細節資料>的呈現常常在資訊系統中出現：在概述資料中，我們呈現「一群」資料的概述，當我們點擊某一筆資料的時候，就會出現細節(detail)資料的全貌。
* members 是一個集合物件，透過 `id` 指定明確物件，近一步呈現某會員的細節資料。

#### lab5.1. 細節資料的頁面設計

Template:

> `my_tennis_club/members/templates/details.html`:

呈現某一個會員的資料
```html=
<!DOCTYPE html>
<html>
<body>
  <h1>{{ mymember.firstname }} {{ mymember.lastname }}</h1>  
  <p>Phone: {{ mymember.phone }}</p>
  <p>Member since: {{ mymember.joined_date }}</p>
  <p>Back to <a href="/members">Members</a></p>
</body>
</html>
```

View:

> `my_tennis_club/members/views.py:`

透過 `Member.objects.get(id = id)` 來獲得`id` 的資訊，然後傳過去`details.html`。注意 `details` 有兩個參數，第二個是 `id`:

```python=
def details(request, id):
  mymember = Member.objects.get(id = id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
```  

第二個參數 `id` 哪裡來的呢？我們的 url 路徑：

> `my_tennis_club/members/urls.py:`

```python=
from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
]
```

其中 `<int:id>` 表示是一個整數變數，並不是固定的路徑。

#### lab5.2. 概述資料的頁面設計

修改 `all_member.html`, 添加 `a` 標記，做出連接：
> `my_tennis_club/members/templates/all_members.html:`

:point_right: 重點在第 9 行的 `a` 標記
```html=
<!DOCTYPE html>
<html>
<body>

<h1>Members</h1>
  
<ul>
  {% for x in mymembers %}
    <li><a href="details/{{ x.id }}">{{ x.firstname }} {{ x.lastname }}</a></li>
  {% endfor %}
</ul>
    
</body>
</html>
```

#### lab5.3. 頁面擴充標記

**主頁面** (Master) 類似製作投影片的母片，把大架構確立出來，細節由擴充頁面來提供。宣告一些「被擴充區塊」，用`{% block 區塊代號 %}`及`{% endblock %}` 標記。以下宣告了 `title` 及 `content` 兩個區塊，等待擴充。

> my_tennis_club/members/templates/master.html:

```html=
<!DOCTYPE html>
<html>
<head>
  <title>{% block title %}{% endblock %}</title>
</head>
<body>

{% block content %}
{% endblock %}

</body>
</html>
```

**擴充頁面**，先在一開始宣告要擴充的頁面（利用`{% extends %}`標記），接下來「覆蓋」個擴充區塊- 同樣用 `{% block 區塊代號 %}`及`{% endblock %}`。

`all_members.html` 是擴充頁面:

> `my_tennis_club/members/templates/all_members.html:`

```html=
{% extends "master.html" %}

{% block title %}
  My Tennis Club - List of all members
{% endblock %}


{% block content %}
  <h1>Members</h1>
  
  <ul>
    {% for x in mymembers %}
      <li><a href="details/{{ x.id }}">{{ x.firstname }} {{ x.lastname }}</a></li>
    {% endfor %}
  </ul>
{% endblock %}
```
* 要擴充 `master.html`
* 覆蓋 `master.html` 中的兩個區塊： `title` 以及 `content` 

`details.html` 也是擴充頁面：

> `my_tennis_club/members/templates/details.html:`

```html=
{% extends "master.html" %}

{% block title %}
  Details about {{ mymember.firstname }} {{ mymember.lastname }}
{% endblock %}


{% block content %}
  <h1>{{ mymember.firstname }} {{ mymember.lastname }}</h1>
  
  <p>Phone {{ mymember.phone }}</p>
  <p>Member since: {{ mymember.joined_date }}</p>
  
  <p>Back to <a href="/members">Members</a></p>
  
{% endblock %}
```

下圖是一個結構的示意（S在此表示一個頁面)，三角形的符號表示一個擴充。

```plantuml
struct master.html {
    - {abstract} title
    - {abstract} content
}

struct all_members.html extends master.html
struct details.html extends master.html
all_members.html .>  details.html

```

See branch **[details](https://github.com/nlhsueh/nlh_tennis_club/tree/details)**

### Lab06: 主畫面

:::success
:football: You will do
* 一個系統的首頁，並且讓其他分頁可以快速回到首頁
* 如何關閉與開啟除錯模式
* 當除錯模式關閉時，如何將系統錯誤引導到錯誤說明頁面。
:::

* 做一個系統的 主畫面- [main.html](https://github.com/nlhsueh/nlh_tennis_club/blob/index/members/templates/main.html); 路由要記得設定 ([urls.py](https://github.com/nlhsueh/nlh_tennis_club/blob/index/members/urls.py))
* 再設定檔 [setting.py](https://github.com/nlhsueh/nlh_tennis_club/blob/index/my_tennis_club/settings.py) 關閉除錯模式 -- 也就是設定 `default=False`。系統出錯時，就不會出現除錯資訊，會自動轉到 `404.html`。
* 修改 [view.py](https://github.com/nlhsueh/nlh_tennis_club/blob/index/members/views.py), 加上 `main(request)` 的導向
* 建立一新檔 [404.html](https://github.com/nlhsueh/nlh_tennis_club/blob/index/members/templates/404.html)-- 撰寫系統出現時，要給使用者的訊息。
* 修改 [master.html](https://github.com/nlhsueh/nlh_tennis_club/blob/index/members/templates/master.html), 加上回到首頁的連接。
* Read [w3school example](https://www.w3schools.com/django/django_add_main.php) for more information.

See branch **[index](https://github.com/nlhsueh/nlh_tennis_club/tree/index)**

:question: 如果不想用預設的 404.html, 該如何設定？ (Ans: see [here](https://www.geeksforgeeks.org/how-to-fix-page-not-found-404-django/))

### Lab07: 查詢會員
:::success
:football: You will learn
* 如何設計一個輸入表單，和後端的 django 互動
* form GET 和 POST 的差異
:::

* 做一個輸入表單，透過 lastname 來查詢會員

#### lab7.1 查詢頁面
> check_member.html: 

```html=
<form action="" method="GET">
  <label for="last_name">Last name:</label><br>
  <input type="text" id="last_name" name="last_name"><br><br>
  <input type="submit" value="Submit">
</form> 
```
或是由後端來做，設計一個 [CheckMemberForm](https://github.com/nlhsueh/nlh_tennis_club/blob/form_get/members/forms.py) - 它是 `forms.Form` 的子類別：
```html=
<form action = "" method = "GET">
    {{ form.as_p }}
    <input type="submit" value='Submit'>
</form>
```
* `as_p` 是將 form 用 p 元件來呈現，其他還有 `as_table`, `as_list`

```plantuml
struct urls.py <<URL>>{
    check_member
}

struct views <<VIEW>> {
    + check_member(request)
}

class CheckMemberForm extends forms.Form {
    last_name: forms.CharField
}
struct check_member.html <<TEMPLATE>>
struct checked_member.html <<TEMPLATE>>
urls.py --> views: check_member

views -> check_member.html:GET
check_member.html -> views:submit
views --> checked_member.html
views ..> CheckMemberForm
check_member.html ..> CheckMemberForm
```
#### lab7.2 路由設定
加上新的路由到 [urls.py](https://github.com/nlhsueh/nlh_tennis_club/blob/form_get/members/urls.py)
```python
path('members/check_member', views.check_member, name='check_member'),
```


#### lab7.3 查詢的處理 (views)

* 第一次呼叫 [views.check_member](https://github.com/nlhsueh/nlh_tennis_club/blob/form_get/members/views.py), 是由 urls 導向過來的，`request.method` 是 `GET`, 但 `request.GET` 是空的。此時我們引導到 [check_member.html](https://github.com/nlhsueh/nlh_tennis_club/blob/form_get/members/templates/check_member.html)
* 當使用者在 `check_member.html` 中輸入 `last_name` 的值並提交後，會再次執行 `views.check_member`, 此時 `request.GET` 會包含使用者在 form 中所填寫的值。我們透過 `Member.objects.filter()` 來找到所有符合條件的物件，在引導到 [checked_members.html](https://github.com/nlhsueh/nlh_tennis_club/blob/form_get/members/templates/checked_members.html).

### Lab08: 用表單新增會員

:::success
:football: You will learn
* POST request 如何被處理，如何將使用者輸入的資料存到資料庫
* ModelForm 的設計與應用
:::
1. 設計一個資料表單 [NewMemberForm](https://github.com/nlhsueh/nlh_tennis_club/blob/form_post/members/forms.py), 可以用來呈現介面，同時儲存到資料庫。記得是繼承 `ModelForm`。
2. 新增路由到 [urls.py](https://github.com/nlhsueh/nlh_tennis_club/blob/form_post/members/urls.py)
3. 設計 [new_member.html](https://github.com/nlhsueh/nlh_tennis_club/blob/form_post/members/templates/new_member.html): 透過 POST 方式，將提交的資料存到資料庫。注意我們是用資料表單來產生介面表單(`form.as_p()`)。
    * `as_p`: as paragraph
    * `as_table`: table
    * `as_ul`: list
    * 資安考量，POST 請求都必須加上 `{% csrf_token %}`
4. 在 [view.py](https://github.com/nlhsueh/nlh_tennis_club/blob/form_post/members/views.py) 中加上 `new_member(request)`: 判斷是 `POST` 請求後，依據取得的資料(`request.POST`)生成一個 `NewMemberForm` 物件，檢查此提交的表單是否正確 (`is_valid`)，確認正確後直接呼叫 `save()` 儲存。
    * 若無法儲存，可以透過 `form.error` 取得錯誤資訊。
    * 如果是 GET 請求，將之轉到 `new_member.html`
5. 無論成功或失敗，都引導到 [new_member_result.html](https://github.com/nlhsueh/nlh_tennis_club/blob/form_post/members/templates/new_member_result.html)

```plantuml
struct urls.py {
    new_member
}

struct views {
    + new_member(request)
}

class NewMemberForm extends forms.ModelForm {}
class Meta {
    model
    fields
    widget
    labels    
}
NewMemberForm *-> Meta
class Member extends Model {
    last_name: forms.CharField
    first_name: forms.CharField
    phone: forms.Integer
    joined_date: forms.DateField    
}
Meta ..> Member
struct new_member.html
struct new_member_result.html
urls.py --> views: new_member

views -> new_member.html: GET
new_member.html -> views: POST
views --> new_member_result.html
views ..> NewMemberForm
new_member.html ..> NewMemberForm
```
See [branch **form_post**](https://github.com/nlhsueh/nlh_tennis_club/tree/form_post)


:question: 輸入的時候如果要一些表單檢查的話該怎麼做？例如 joined_date 不可晚於今天。[Hint](https://www.geeksforgeeks.org/python-form-validation-using-django/)。

## 網球俱樂部 (III)

### ex01_age: tag if
:::success
:football: 年齡分組
* 在 model 中為會員增加一個欄位 age
* 修改 all members, 會分兩個區塊，一個是小於 20 歲的青少年組，一個是超過 20 歲的成人組。

學習重點
* template tag: if
* `py manage.py makemigrations`; `py manage.py migrate`

:::
```plantuml
class Member {
    - lastname
    - firstname
    - phone
    - joined_date
    - age
}
```
Code:
```html=
{% for x in mymembers %}
    {% if x.age < 20 %}
        <li><a href="details/{{ x.id }}">{{ x.firstname }} 
        {{ x.lastname }}</a>, {{x.age}}</li>
        {% endif %}
{% endfor %}
```    

<img style="border:1px solid; width:280px" src="https://hackmd.io/_uploads/HkvY2jmGR.png"><br>

See [branch **age**](https://github.com/nlhsueh/nlh_tennis_club/tree/age)

### ex02_court: enum
:::success
:football: 網球場
* 在 model 中增加一個資料球場: 球場名稱、球場型態（草地、硬地、泥地、地毯)，所在城市。
* 修改系統，可以透過 /courts 列出所有的球場，點擊該球場可以看到球場細部資料。

學習重點
* 一個系統可以有多個 app (子系統)
* 資料庫中列舉性的資料型態處理
:::
Hint
* 建立 courts 的 App (`py manage.py startapp courts`)
* 建立一個 Courts 的 model
* 參考 members app 的做法，加入對 courts 的程式
* 使用 choices 來做列舉型態

```plantuml
package nlh_tennis_club {
    package members {
        
    }
    package courts {
        struct models.py
        struct urls.py
        struct views.py
        package templates {
            struct all_courts.html
            struct court_details.html
            struct court_main.html
        }
    }
}
```

> See [Court](https://github.com/nlhsueh/nlh_tennis_club/blob/court/courts/models.py) model

<img style="border:1px solid; width:280px" src="https://hackmd.io/_uploads/SyMmCsXMR.png"><br>

<img style="border:1px solid; width:280px" src="https://hackmd.io/_uploads/SJxB0smG0.png"><br>

See [branch **court**](https://github.com/nlhsueh/nlh_tennis_club/tree/court)

### ex03_web

:::success
:football: 我要預約
* 使用者可以輸入帳號密碼登入
* 登入後每個球場後面有個"預約"的按鈕，點擊後會進入到預約頁面：包含預約日期、時間及長度。
* 可以看到預約的狀況：預約者、日期、地點。

學習重點:
* 登入表單的製作; 帳號認證的執行與檢查
* 表單輸入對於防呆的處理 (clean data)
* 需登入才能執行動作處理及導向
* 資料庫外鍵 (foreign key) 的設定
:::

See [branch **web**](https://github.com/nlhsueh/nlh_tennis_club/tree/web); [readme.md 解說](https://github.com/nlhsueh/nlh_tennis_club/blob/web/readme.md)
#### Login process
```plantuml
package web{
    struct urls.py {
        /login
        /logout
    }
    struct views.py {
        +login(r)
        +logout(r)
    }
    package templates {
        struct login.html
    }
    class LoginForm {
        - username
        - password
    }
}
struct main.html

urls.py --> views.py
login.html <-> views.py:GET/POST
views.py --> main.html: [login ok]; /logout
LoginForm <. views.py
LoginForm <. login.html
```
#### Booking process:
```plantuml
class Booking <<Model>>{
    court: Court
    user: User
    date: DateField
}

class BookingForm <<ModelForm>>

struct views {
    +booking(r,c)@login
    +mybooking(r)@login
}
class User <<Model>>
struct booking.html <<template>>
struct booking_result.html <<template>>
struct urls.py <<url>>
urls.py --> views
Court <--* Booking:foreign_key
Booking *--> User:foreign_key
views --> booking.html:GET
booking.html --> views:POST
views --> booking_result.html
views .> BookingForm
views .> Booking

BookingForm .> Booking
```


### ex04_static_files

:::success
:football: css 與 images
* 用 CSS 和圖片美化網頁

學習重點
* 與 CSS 的合用
:::
See [branch **static**](https://github.com/nlhsueh/nlh_tennis_club/tree/static)

* [readme.md 解說](https://github.com/nlhsueh/nlh_tennis_club/blob/static/readme.md)

### ex05_bootstrap

:::success
:football: bootstrap
* 使用 bootstrap 美化

學習重點
* bootstrap 的合用
:::
See [branch **bs**](https://github.com/nlhsueh/nlh_tennis_club/tree/bs)

* [readme.md 解說](https://github.com/nlhsueh/nlh_tennis_club/blob/bs/readme.md)

<img src=https://hackmd.io/_uploads/rJ2krF0LT.png width=400>


### ex06_validation
:::success
:football: 輸入驗證
* 預借網球場時，需要寫理由，理由必須大於 10 個字。

學習重點：
* 如何在 form 中宣告方法，撰寫表單輸入時的驗證邏輯。
:::
See [branch **validation**](https://github.com/nlhsueh/nlh_tennis_club/tree/validation)

* [readme.md 解說](https://github.com/nlhsueh/nlh_tennis_club/blob/validation/readme.md)

<img src="https://hackmd.io/_uploads/rkjBGi-Pp.png" width='350'>

### ex07_img
:::success
:football: 多媒體欄位
* 在 admin 的介面，直接設定網球場的圖片; 並且之後可以顯示。

學習重點：
* 如何宣告圖形檔的資料欄位 ImageField; 
:::
See [branch **img**](https://github.com/nlhsueh/nlh_tennis_club/tree/img)

* 此版本需要安裝 pillow `py -m pip install pillow` 
* [readme.md 解說](https://github.com/nlhsueh/nlh_tennis_club/blob/img/readme.md)

<img src="https://hackmd.io/_uploads/SyjVqofPp.png" width="300">

### ex08_bind_user
:::success
:football: 把 user 和 member 綁定
* Member 資料中增加 user 連接
* user 登入後可以查看我的預約

學習重點
* 資料庫設計的資料表如何與系統的 user 做綁定
:::
See [branch **bind_user**](https://github.com/nlhsueh/nlh_tennis_club/tree/bind_user)

* [readme.md 解說](https://github.com/nlhsueh/nlh_tennis_club/blob/bind_user/readme.md)

列出會員
<img src="https://hackmd.io/_uploads/r19Q1i8Da.png" width="200">

我的預約：
<img src="https://hackmd.io/_uploads/rJaD1sLw6.png" width="400">

## HW/Quiz

### HW-Baseball

:::success
:basketball: 棒球網站

* 呈現球隊的所有球員，包含姓名、身高體重等基本資料，以及守備位置
* 如果是野手，呈現打擊率、全壘打個數、被三振率等。
* 如果是投手，呈現勝敗場數，以及失分率（）
* 首頁可以選擇(1) 列出所有球員 (2) 點選後觀看球員資料 (3) 查詢球員資料 (4) 新增球員資料
* 要用網頁母版來做到頁面共享的功能
:::


### HW-BMI

:::success
:basketball: 設計一個表單，可以輸入一群人的姓名、身高、體重。提交後會存到資料庫中，並進行下一筆資料的輸入。

* 點選統計：會呈現 BMI 過高的人、過低的人、以及正常的人的資訊。
* 點選繼續編輯：會回到編輯表單繼續加入資料
* 點選隨機輸入：會隨機輸入10筆資料，包含姓名身高體重等，都透過亂數輸入一些合理的值。(建議設計姓與名的詞典，組合出有意義的名字)
:::

### Quiz-gender
:::success
:basketball: 下載並實作以下需求： 
* 下載 form_post 版本，安裝並啟動成功 (**50%**)
* 加上並呈現性別 (**20%**)
  * 將 member 加上 gender 的性別屬性，其型態是列舉型態的：男、女。現有資料中，設定至少兩人是男，兩人是女。
  * 修改 http://127.0.0.1:8000/members/, 點擊後會出現男女的分類，而非年齡的分類。
* 查詢性別 (**20%**)
  * 首頁 Member 下，加上一個 Query 的連結，點擊後出現可以依據男女查詢畫面，用下拉式，或是 radio 的方式選擇，按下提交後出現對應的會員。
* 透過修改 master.html 改變整體版面（如下方畫面）(**10%**)
* [完整題目](https://docs.google.com/document/d/1JPLj68nsLcJrFOJkfGcrby2FLoX5SVWPYsSSTYCzRoY/edit?usp=sharing)
:::
* [Hint solution](https://github.com/nlhsueh/nlh_tennis_club/tree/gender?tab=readme-ov-file)

### Exam- Friends web
:::success
* 112-2 final exam- coding part
    * [題目](https://github.com/nlhsueh/friends_web/blob/exam_112_2/readme.md); [Github程式](https://github.com/nlhsueh/friends_web/tree/exam_112_2) (branch: **exam_112_2**)
    * [解答](https://github.com/nlhsueh/friends_web/tree/solution_more) (branch: **solution_more**)
* Extension:
    * 修改 /seasons 頁面，始之一頁只呈現一季的內容，有 prev 及 next 的連接，可以到上一季、下一季的內容。需處理到頭尾的問題（出現錯誤訊息）
    * 可以登入/登出。登入後可以在逛每一集 (/episodes) 時加上我的最愛的註記。加上一個 My Favorate 呈現我喜歡的頁面。
    * 同上，在 /episodes 出現每一集時，上方有一個 season 及 episode 的下拉選單，方便我們直接跳到某一季的某一集。
:::


## 其他

### 五倍券 (VH5000) 實例 (略)

* [Unit 1 App](https://docs.google.com/presentation/d/1f4gz1_qZsRjub5oxov3xKzgxlSeYa1zIrsuGGqPCxmQ/edit?usp=sharing)
* [Unit 2 List view](https://docs.google.com/presentation/d/1-NXJa4RteGJrqExjBwGQMd7ZlAYrU0STjT871dxatuw/edit?usp=sharing)
* [Unit 3 Form](https://docs.google.com/presentation/d/1-NXJa4RteGJrqExjBwGQMd7ZlAYrU0STjT871dxatuw/edit?usp=sharing)
* [Unit 4 Auth](https://docs.google.com/presentation/d/1K1Y1Yd6hafMwE8Q7o79PJPSPZHIVUyWyTfNUXrYcL58/edit?usp=sharing)

VH5000 on GitHub:
* https://github.com/nienlinh/vh5000

```
// 把專案複製到你的電腦
git clone https://github.com/nienlinh/vh5000.git

// 檢查一下目前在的版本
git branch

// 切換到 dj01a 版本
git checkout dj01a

// 啟動伺服器
python manage.py runserver

// 切換到 dj03 版本
git checkout dj03

// 安裝 Pillow 套件
python -m pip install Pillow

// 啟動伺服器
python manage.py runserver
```

### 112-1 web dev projects
- [in **DemoX**](https://demox.tw/curation/detail/?id=102)
- [網球會員網](https://demox.tw/idea/detail/?id=408)- 簡單的範例
- [打地鼠](https://demox.tw/idea/detail/?id=1322)- 透過Django建立一個打地鼠的遊戲網站。 具有註冊、登入、登出、排行榜功能。 透過滑鼠點擊方式打地鼠在有限時間內獲得分數，個人的最佳成績會顯示在排行榜上，可以查看自己的排名與分數。
- [記帳行事曆](https://demox.tw/idea/detail/?id=1327)- 帶有記帳功能的行事曆，能夠展示事件，還能將重要的事件標註，將在一跑馬燈中列出以提醒使用者，記帳會顯示出收入支出與總額，也會將細項一一列出，有著深淺主題，在切換不同的頁面時，主題會同步變更。
- [小說倉庫](https://demox.tw/idea/detail/?id=1320)- 小說網站，可以觀看小說，寫小說，評論小說
- [IP 設備控管](https://demox.tw/idea/detail/?id=1324)- 蒐集各個 IP 對應的裝置、軟體、系統、擁有者並分類，以方便裝置管理
- [ChuChat](https://demox.tw/idea/detail/?id=1329)- 為了打破傳統聊天應用的界限，結合多個 AI 聊天機器人 API，讓使用者能夠在單一平台上與不同的聊天機器人互動，獲取更全面、多元的資訊，同時創造一個輕鬆、趣味且高效的聊天體驗。
- 電影院訂位- 查詢電影院訂位狀況並進行訂位
- 漫畫書購物網- 查詢並購買漫畫書
- 百搭衣物販售網頁- 購衣網
- 台灣旅遊網- 旅遊景點
- 簡單的縮網址
- Bloggin Platform 
- 副業投資
- 租相機系統
- 美味吐司到你家
- 遊戲地獄
- 圖書館借閱還書系統
- 食譜網站創建
- 預訂飯店網站


Reference web books
- [Web dev with django by **Ben Shaw**](https://github.com/PacktPublishing/Web-Development-with-Django-Second-Edition)
    - github code
- [Three Django books by **William Vincent**](https://www.amazon.com/stores/William-S.-Vincent/author/B07B38Y8SG?language=zh_TW&ref=sr_ntt_srch_lnk_1&qid=1706505875&sr=1-1&isDramIntegrated=true&shoppingPortalEnabled=true)
    - [for *beginners*](https://www.amazon.com/William-S-Vincent/dp/1735467200/?_encoding=UTF8&pd_rd_w=pgO4G&content-id=amzn1.sym.cf86ec3a-68a6-43e9-8115-04171136930a&pf_rd_p=cf86ec3a-68a6-43e9-8115-04171136930a&pf_rd_r=147-0863838-6848330&pd_rd_wg=NdQpw&pd_rd_r=9635f6ae-7835-4e3f-8e09-10d66d4075a0&ref_=aufs_ap_sc_dsk)
    - [for *professionals*](https://www.amazon.com/William-S-Vincent/dp/1735467235/?_encoding=UTF8&pd_rd_w=pgO4G&content-id=amzn1.sym.cf86ec3a-68a6-43e9-8115-04171136930a&pf_rd_p=cf86ec3a-68a6-43e9-8115-04171136930a&pf_rd_r=147-0863838-6848330&pd_rd_wg=NdQpw&pd_rd_r=9635f6ae-7835-4e3f-8e09-10d66d4075a0&ref_=aufs_ap_sc_dsk)
    - [for *API*](https://www.amazon.com/William-S-Vincent/dp/1735467227/?_encoding=UTF8&pd_rd_w=pgO4G&content-id=amzn1.sym.cf86ec3a-68a6-43e9-8115-04171136930a&pf_rd_p=cf86ec3a-68a6-43e9-8115-04171136930a&pf_rd_r=147-0863838-6848330&pd_rd_wg=NdQpw&pd_rd_r=9635f6ae-7835-4e3f-8e09-10d66d4075a0&ref_=aufs_ap_sc_dsk)

