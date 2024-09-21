# <a style="text-decoration: none"><center>**POSITIVE API**</center></a>
## <center>**Servidor do Positive**</center>

## <a style="text-decoration: none">Description :</a>
<p style="text-align: justify">Servidor do Positive.</p>

<p id="summary"></p>
<h2> SUMMARY BY MODEL:</h2>
<ol>
    <li><a href=#welcome style="text-decoration: none;">Welcome</a></li>
    <li><a href=#meetings style="text-decoration: none;">Meetings</a></li>
    <li><a href=#albummeeting style="text-decoration: none;">Album Meeting</a></li>
    <li><a href=#imagealbummeeting style="text-decoration: none;">Image Album Meeting</a></li>
    <li><a href=#videomeeting style="text-decoration: none;">Video Meeting</a></li>
    <li><a href=#course style="text-decoration: none;">Course</a></li>
    <li><a href=#videocourse style="text-decoration: none;">Video Course</a></li>
    <li><a href=#commentcourse style="text-decoration: none;">Comment Course</a></li>
    <li><a href=#news style="text-decoration: none;">News</a></li>
    <li><a href=#ebook style="text-decoration: none;">E-Book</a></li>
    <li><a href=#planner style="text-decoration: none;">Planner</a></li>
    <li><a href=#user style="text-decoration: none;">User</a></li>
    <li><a href=#useranalysis style="text-decoration: none;">User Analysis</a></li>
</ol>

</br>
</br>

### Local baseUrl:
```bash
http://127.0.0.1:9000/positive/
```

</br>

## <a style="text-decoration: none">Models and endpoints :</a>
<p id=welcome></p>
<h2 style="color: orange">Welcome</h2>
<a href=#summary>Voltar ao topo</a>

### baseUrl model:
```bash
{BaseUrl}/welcome/
```

## Fields:
```bash
    title = String
    date = DateTime
    cover = File
    video = File - Video
    description = String
```

## Endpoints:
### Token
- `{BaseUrlModel}/`: Endpoint to create welcome - method post.
- `{BaseUrlModel}/<uuid:id>/`: Endpoint to retrieve data from a welcome - method get.
- `{BaseUrlModel}/`: Endpoint to collect data from all welcomes - method get.
- `{BaseUrlModel}/<uuid:id>/`: Endpoint used to partial update a welcome's data - method patch.

### Action: CREATE WELCOME
### Method: POST
### Endpoint
```bash
{BaseUrlModel}/
```
### Authentication
```bash
Bearer token
```
### Body  <span style="color: red">[required]</span>
```bash
{
	"title" : "Bem vindos a Positive",
    "date" : "2024-09-20",
    "cover" : "file Cover",
    "video" : "file Video",
    "description" : "Boas vindas ao site da Positive"
}
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 201
```
```bash
{
    ...welcome data
}
```

### Action: RETRIEVE WELCOME
### Method: GET
### Endpoint
```bash
{BaseUrlModel}/pk/
```
### Authentication
```bash
Bearer token
```
### Body
```bash
no body
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
{
    ...welcome data
}
```
### Action: LIST WELCOMES
### Method: GET
### Endpoint
```bash
{BaseUrlModel}/
```
### Authentication
```bash
Bearer token
```
### Body
```bash
no body
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
[
    {
    ...welcome data
    },
    {
    ...welcome data
    },
    ...
]
```
### Action: PARTIAL UPDATE WELCOME
### Method: PATCH
### Endpoint
```bash
{BaseUrlModel}/pk/
```
### Authentication
```bash
Bearer token
```
### Body  <span style="color: red">[required]</span>
```bash
{
	"title": "BEM VINDOS A POSITIVE",
    ... more fields if necessary
}
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
{
    ... welcome data updated
}
```

<p id=meetings></p>
<h2 style="color: green">Meeting</h2>
<a href=#summary>Voltar ao topo</a>

### baseUrl model:
```bash
{BaseUrl}/meeting/
```

## Fields:
```bash
    title = String
    date = DateTime
    picture = Image
    description = String
```

## Endpoints:
### Token
- `{BaseUrlModel}/`: Endpoint to create meeting - method post.
- `{BaseUrlModel}/<uuid:id>/`: Endpoint to retrieve data from a meeting - method get.
- `{BaseUrlModel}/`: Endpoint to collect data from all meetings - method get.
- `{BaseUrlModel}/<uuid:id>/`: Endpoint used to partial update a meeting's data - method patch.

### Action: CREATE MEETING
### Method: POST
### Endpoint
```bash
{BaseUrlModel}/
```
### Authentication
```bash
Bearer token
```
### Body  <span style="color: red">[required]</span>
```bash
{
	"title" : "Bem vindos a Positive",
    "date" : "2024-09-20",
    "picture" : "file Picture",
    "description" : "Boas vindas ao site da Positive"
}
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 201
```
```bash
{
    ...picture data
}
```

### Action: RETRIEVE MEETING
### Method: GET
### Endpoint
```bash
{BaseUrlModel}/pk/
```
### Authentication
```bash
Bearer token
```
### Body
```bash
no body
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
{
    ...picture data
}
```
### Action: LIST MEETING
### Method: GET
### Endpoint
```bash
{BaseUrlModel}/
```
### Authentication
```bash
Bearer token
```
### Body
```bash
no body
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
[
    {
    ...picture data
    },
    {
    ...picture data
    },
    ...
]
```
### Action: PARTIAL UPDATE MEETING
### Method: PATCH
### Endpoint
```bash
{BaseUrlModel}/pk/
```
### Authentication
```bash
Bearer token
```
### Body  <span style="color: red">[required]</span>
```bash
{
	"title": "BEM VINDOS A POSITIVE",
    ... more fields if necessary
}
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
{
    ... picture data updated
}
```

<p id=albummeeting></p>
<h2 style="color: brown">Album Meeting</h2>
<a href=#summary>Voltar ao topo</a>

### baseUrl model:
```bash
{BaseUrl}/album_meeting/
```

## Fields:
```bash
    title = String
    date = DateTime
    meeting = Meeting id
    free = Boolean
```

## Endpoints:
### Token
- `{BaseUrlModel}/`: Endpoint to create album meeting - method post.
- `{BaseUrlModel}/<uuid:id>/`: Endpoint to retrieve data from a album meeting - method get.
- `{BaseUrlModel}/`: Endpoint to collect data from all album meetings - method get.
- `{BaseUrlModel}/<uuid:id>/`: Endpoint used to partial update a album meeting's data - method patch.

### Action: CREATE ALBUM MEETING
### Method: POST
### Endpoint
```bash
{BaseUrlModel}/
```
### Authentication
```bash
Bearer token
```
### Body  <span style="color: red">[required]</span>
```bash
{
	"title" : "Bem vindos a Positive",
    "date" : "2024-09-20",
    "meeting" : Meeting id,
    "free" : false,
}
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 201
```
```bash
{
    ...album meeting data
}
```

### Action: RETRIEVE ALBUM MEETING
### Method: GET
### Endpoint
```bash
{BaseUrlModel}/pk/
```
### Authentication
```bash
Bearer token
```
### Body
```bash
no body
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
{
    ...album meeting data
}
```
### Action: LIST ALBUM MEETINGS
### Method: GET
### Endpoint
```bash
{BaseUrlModel}/
```
### Authentication
```bash
Bearer token
```
### Body
```bash
no body
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
[
    {
    ...album meeting data
    },
    {
    ...album meeting data
    },
    ...
]
```
### Action: PARTIAL UPDATE ALBUM MEETING
### Method: PATCH
### Endpoint
```bash
{BaseUrlModel}/pk/
```
### Authentication
```bash
Bearer token
```
### Body  <span style="color: red">[required]</span>
```bash
{
	"title": "Album da reunião do dia das mulheres",
    ... more fields if necessary
}
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
{
    ... album meeting data updated
}
```

<p id=imagealbummeeting></p>
<h2 style="color: pink">Image Album Meeting</h2>
<a href=#summary>Voltar ao topo</a>

### baseUrl model:
```bash
{BaseUrl}/image_album_meeting/
```

## Fields:
```bash
    title = String
    date = DateTime
    picture = Image
    album = ALbumMeeting Id
    free = Boolean
```

## Endpoints:
### Token
- `{BaseUrlModel}/`: Endpoint to create image album meeting - method post.
- `{BaseUrlModel}/<uuid:id>/`: Endpoint to retrieve data from a image album meeting - method get.
- `{BaseUrlModel}/`: Endpoint to collect data from all image album meetings - method get.
- `{BaseUrlModel}/<uuid:id>/`: Endpoint used to partial update a image album meeting's data - method patch.

### Action: CREATE IMAGE ALBUM MEETING
### Method: POST
### Endpoint
```bash
{BaseUrlModel}/
```
### Authentication
```bash
Bearer token
```
### Body  <span style="color: red">[required]</span>
```bash
{
	"title" : "Foto 1",
    "date" : "2024-09-20",
    "picture" : "file Picture",
    "meeting" : AlbumMeeting id,
    "free" : false,
}
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 201
```
```bash
{
    ...image album meeting data
}
```

### Action: RETRIEVE IMAGE ALBUM MEETING
### Method: GET
### Endpoint
```bash
{BaseUrlModel}/pk/
```
### Authentication
```bash
Bearer token
```
### Body
```bash
no body
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
{
    ...image album meeting data
}
```
### Action: LIST IMAGE ALBUM MEETINGS
### Method: GET
### Endpoint
```bash
{BaseUrlModel}/
```
### Authentication
```bash
Bearer token
```
### Body
```bash
no body
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
[
    {
    ...image album meeting data
    },
    {
    ...image album meeting data
    },
    ...
]
```
### Action: PARTIAL UPDATE IMAGE ALBUM MEETING
### Method: PATCH
### Endpoint
```bash
{BaseUrlModel}/pk/
```
### Authentication
```bash
Bearer token
```
### Body  <span style="color: red">[required]</span>
```bash
{
	"title": "Foto do almoço",
    ... more fields if necessary
}
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
{
    ... image album meeting data updated
}
```

<p id=videomeeting></p>
<h2 style="color: gray">Video Meeting</h2>
<a href=#summary>Voltar ao topo</a>

### baseUrl model:
```bash
{BaseUrl}/video_meeting/
```

## Fields:
```bash
    title = String
    date = DateTime
    video = File
    description = String
    meeting = Meeting id
    free = Boolean
```

## Endpoints:
### Token
- `{BaseUrlModel}/`: Endpoint to create video meeting - method post.
- `{BaseUrlModel}/<uuid:id>/`: Endpoint to retrieve data from a video meeting - method get.
- `{BaseUrlModel}/`: Endpoint to collect data from all video meetings - method get.
- `{BaseUrlModel}/<uuid:id>/`: Endpoint used to partial update a video meeting's data - method patch

### Action: CREATE VIDEO MEETING
### Method: POST
### Endpoint
```bash
{BaseUrlModel}/
```
### Authentication
```bash
Bearer token
```
### Body  <span style="color: red">[required]</span>
```bash
{
	"title" : "Foto 1",
    "date" : "2024-09-20",
    "video" : "file Video",
    "description" : "Video do almoço do dia das mulheres",
    "meeting" : Meeting id
    "free" : false,
}
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 201
```
```bash
{
    ...video meeting data
}
```

### Action: RETRIEVE VIDEO MEETING
### Method: GET
### Endpoint
```bash
{BaseUrlModel}/pk/
```
### Authentication
```bash
Bearer token
```
### Body
```bash
no body
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
{
    ...video meeting data
}
```
### Action: LIST VIDEO MEETINGS
### Method: GET
### Endpoint
```bash
{BaseUrlModel}/
```
### Authentication
```bash
Bearer token
```
### Body
```bash
no body
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
[
    {
    ...video meeting data
    },
    {
    ...video meeting data
    },
    ...
]
```
### Action: PARTIAL UPDATE VIDEO MEETING
### Method: PATCH
### Endpoint
```bash
{BaseUrlModel}/pk/
```
### Authentication
```bash
Bearer token
```
### Body  <span style="color: red">[required]</span>
```bash
{
	"title": "Foto do almoço",
    ... more fields if necessary
}
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
{
    ... video meeting data updated
}
```

<p id=course></p>
<h2 style="color: blue">Course</h2>
<a href=#summary>Voltar ao topo</a>

### baseUrl model:
```bash
{BaseUrl}/course/
```

## Fields:
```bash
    title = String
    date = DateTime
    cover = Image
    file = File
    description = String
    free = Boolean
```

## Endpoints:
### Token
- `{BaseUrlModel}/`: Endpoint to create course - method post.
- `{BaseUrlModel}/<uuid:id>/`: Endpoint to retrieve data from a course - method get.
- `{BaseUrlModel}/`: Endpoint to collect data from all courses - method get.
- `{BaseUrlModel}/<uuid:id>/`: Endpoint used to partial update a course's data - method patch

### Action: CREATE COURSE
### Method: POST
### Endpoint
```bash
{BaseUrlModel}/
```
### Authentication
```bash
Bearer token
```
### Body  <span style="color: red">[required]</span>
```bash
{
	"title" : "Curso de liderança",
    "date" : "2024-09-20",
    "cover" : "file Cover",
    "file" : "file PDF",
    "description" : "Com de liderança com a dra. Luiza Mesquita",
    "free" : false,
}
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 201
```
```bash
{
    ...course data
}
```

### Action: RETRIEVE COURSE
### Method: GET
### Endpoint
```bash
{BaseUrlModel}/pk/
```
### Authentication
```bash
Bearer token
```
### Body
```bash
no body
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
{
    ...course data
}
```
### Action: LIST COURSE
### Method: GET
### Endpoint
```bash
{BaseUrlModel}/
```
### Authentication
```bash
Bearer token
```
### Body
```bash
no body
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
[
    {
    ...course data
    },
    {
    ...course data
    },
    ...
]
```
### Action: PARTIAL UPDATE COURSE
### Method: PATCH
### Endpoint
```bash
{BaseUrlModel}/pk/
```
### Authentication
```bash
Bearer token
```
### Body  <span style="color: red">[required]</span>
```bash
{
	"free": true,
    ... more fields if necessary
}
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
{
    ... course data updated
}
```

<p id=videocourse></p>
<h2 style="color: yellow">Video Course</h2>
<a href=#summary>Voltar ao topo</a>

### baseUrl model:
```bash
{BaseUrl}/video_course/
```

## Fields:
```bash
    title = String
    date = DateTime
    video = Video
    description = String
    course = Course Id
    free = Boolean
```

## Endpoints:
### Token
- `{BaseUrlModel}/`: Endpoint to create video course - method post.
- `{BaseUrlModel}/<uuid:id>/`: Endpoint to retrieve data from a video course - method get.
- `{BaseUrlModel}/`: Endpoint to collect data from all video courses - method get.
- `{BaseUrlModel}/<uuid:id>/`: Endpoint used to partial update a video course's data - method patch

### Action: CREATE VIDEO COURSE
### Method: POST
### Endpoint
```bash
{BaseUrlModel}/
```
### Authentication
```bash
Bearer token
```
### Body  <span style="color: red">[required]</span>
```bash
{
	"title" : "Curso de liderança",
    "date" : "2024-09-20",
    "video" : "file Video",
    "description" : "Com de liderança com a dra. Luiza Mesquita",
    "course" : Course id,
    "free" : false,
}
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 201
```
```bash
{
    ...video course data
}
```

### Action: RETRIEVE VIDEO COURSE
### Method: GET
### Endpoint
```bash
{BaseUrlModel}/pk/
```
### Authentication
```bash
Bearer token
```
### Body
```bash
no body
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
{
    ...video course data
}
```
### Action: LIST VIDEO COURSE
### Method: GET
### Endpoint
```bash
{BaseUrlModel}/
```
### Authentication
```bash
Bearer token
```
### Body
```bash
no body
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
[
    {
    ...video course data
    },
    {
    ...video course data
    },
    ...
]
```
### Action: PARTIAL UPDATE VIDEO COURSE
### Method: PATCH
### Endpoint
```bash
{BaseUrlModel}/pk/
```
### Authentication
```bash
Bearer token
```
### Body  <span style="color: red">[required]</span>
```bash
{
	"free": true,
    ... more fields if necessary
}
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
{
    ... video course data updated
}
```

<p id=commentcourse></p>
<h2 style="color: white">Comment Course</h2>
<a href=#summary>Voltar ao topo</a>

### baseUrl model:
```bash
{BaseUrl}/comment_course/
```

## Fields:
```bash
    user = User Id
    course = Course Id
    date = DateTime
    message = String
    free =  Boolean
```

## Endpoints:
### Token
- `{BaseUrlModel}/`: Endpoint to create comment course - method post.
- `{BaseUrlModel}/<uuid:id>/`: Endpoint to retrieve data from a comment course - method get.
- `{BaseUrlModel}/`: Endpoint to collect data from all comment courses - method get.
- `{BaseUrlModel}/<uuid:id>/`: Endpoint used to partial update a comment course's data - method patch

### Action: CREATE COMMENT COURSE
### Method: POST
### Endpoint
```bash
{BaseUrlModel}/
```
### Authentication
```bash
Bearer token
```
### Body  <span style="color: red">[required]</span>
```bash
{
	"user" : User id,
    "course" : Course id,
    "date" : "2024-09-20",
    "message" : "Curso muito bom",
    "free" : false,
}
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 201
```
```bash
{
    ...comment course data
}
```

### Action: RETRIEVE COMMENT COURSE
### Method: GET
### Endpoint
```bash
{BaseUrlModel}/pk/
```
### Authentication
```bash
Bearer token
```
### Body
```bash
no body
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
{
    ...comment course data
}
```
### Action: LIST COMMENT COURSE
### Method: GET
### Endpoint
```bash
{BaseUrlModel}/
```
### Authentication
```bash
Bearer token
```
### Body
```bash
no body
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
[
    {
    ...comment course data
    },
    {
    ...comment course data
    },
    ...
]
```
### Action: PARTIAL UPDATE COMMENT COURSE
### Method: PATCH
### Endpoint
```bash
{BaseUrlModel}/pk/
```
### Authentication
```bash
Bearer token
```
### Body  <span style="color: red">[required]</span>
```bash
{
	"message": "O video 1 desse curso é muito bom.",
    ... more fields if necessary
}
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
{
    ... comment course data updated
}
```

<p id=news></p>
<h2 style="color: Darkblue">News</h2>
<a href=#summary>Voltar ao topo</a>

### baseUrl model:
```bash
{BaseUrl}/news/
```

## Fields:
```bash
    title = String
    date = DateTime
    picture = Image
    description = String
    
```

## Endpoints:
### Token
- `{BaseUrlModel}/`: Endpoint to create news - method post.
- `{BaseUrlModel}/<uuid:id>/`: Endpoint to retrieve data from a news - method get.
- `{BaseUrlModel}/`: Endpoint to collect data from all news - method get.
- `{BaseUrlModel}/<uuid:id>/`: Endpoint used to partial update a news's data - method patch

### Action: CREATE NEWS
### Method: POST
### Endpoint
```bash
{BaseUrlModel}/
```
### Authentication
```bash
Bearer token
```
### Body  <span style="color: red">[required]</span>
```bash
{
	"title" : "Curso de liderança M2",
    "date" : "2024-09-20",
    "picture" : "file Picture",
    "description" : "Modulo 2 do curso de liderança"
}
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 201
```
```bash
{
    ...news data
}
```

### Action: RETRIEVE NEWS
### Method: GET
### Endpoint
```bash
{BaseUrlModel}/pk/
```
### Authentication
```bash
Bearer token
```
### Body
```bash
no body
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
{
    ...news data
}
```
### Action: LIST NEWS
### Method: GET
### Endpoint
```bash
{BaseUrlModel}/
```
### Authentication
```bash
Bearer token
```
### Body
```bash
no body
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
[
    {
    ...news data
    },
    {
    ...news data
    },
    ...
]
```
### Action: PARTIAL UPDATE NEWS
### Method: PATCH
### Endpoint
```bash
{BaseUrlModel}/pk/
```
### Authentication
```bash
Bearer token
```
### Body  <span style="color: red">[required]</span>
```bash
{
	"description": "Proxima semana chegam novos cursos",
    ... more fields if necessary
}
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
{
    ... news data updated
}
```

<p id=ebook></p>
<h2 style="color: Darkgreen">E-Book</h2>
<a href=#summary>Voltar ao topo</a>

### baseUrl model:
```bash
{BaseUrl}/ebook/
```

## Fields:
```bash
    title = String
    date = DateTime
    cover = Image
    file = FIle
    free = Boolean
```

## Endpoints:
### Token
- `{BaseUrlModel}/`: Endpoint to create ebook - method post.
- `{BaseUrlModel}/<uuid:id>/`: Endpoint to retrieve data from a ebook - method get.
- `{BaseUrlModel}/`: Endpoint to collect data from all ebook - method get.
- `{BaseUrlModel}/<uuid:id>/`: Endpoint used to partial update a ebook's data - method patch

### Action: CREATE E-BOOK
### Method: POST
### Endpoint
```bash
{BaseUrlModel}/
```
### Authentication
```bash
Bearer token
```
### Body  <span style="color: red">[required]</span>
```bash
{
	"title" : "PDF curso de liderança",
    "date" : "2024-09-20",
    "cover" : "file Cover",
    "file" : "file PDF",
    "free" : false,
}
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 201
```
```bash
{
    ...e-book data
}
```

### Action: RETRIEVE E-BOOK
### Method: GET
### Endpoint
```bash
{BaseUrlModel}/pk/
```
### Authentication
```bash
Bearer token
```
### Body
```bash
no body
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
{
    ...e-book data
}
```
### Action: LIST E-BOOK
### Method: GET
### Endpoint
```bash
{BaseUrlModel}/
```
### Authentication
```bash
Bearer token
```
### Body
```bash
no body
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
[
    {
    ...e-book data
    },
    {
    ...e-book data
    },
    ...
]
```
### Action: PARTIAL UPDATE E-BOOK
### Method: PATCH
### Endpoint
```bash
{BaseUrlModel}/pk/
```
### Authentication
```bash
Bearer token
```
### Body  <span style="color: red">[required]</span>
```bash
{
	"free": true,
    ... more fields if necessary
}
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
{
    ... e-book data updated
}
```

<p id=planner></p>
<h2 style="color: Darkred">Planner</h2>
<a href=#summary>Voltar ao topo</a>

### baseUrl model:
```bash
{BaseUrl}/planner/
```

## Fields:
```bash
    title = String
    date = DateTime
    cover = Image
    file = FIle
    free = Boolean
```

## Endpoints:
### Token
- `{BaseUrlModel}/`: Endpoint to create planner - method post.
- `{BaseUrlModel}/<uuid:id>/`: Endpoint to retrieve data from a planner - method get.
- `{BaseUrlModel}/`: Endpoint to collect data from all planner - method get.
- `{BaseUrlModel}/<uuid:id>/`: Endpoint used to partial update a planner's data - method patch

### Action: CREATE PLANNER
### Method: POST
### Endpoint
```bash
{BaseUrlModel}/
```
### Authentication
```bash
Bearer token
```
### Body  <span style="color: red">[required]</span>
```bash
{
	"title" : "Planner do video 1 do curso de liderança",
    "date" : "2024-09-20",
    "cover" : "file Cover",
    "file" : "file PDF",
    "free" : false,
}
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 201
```
```bash
{
    ...planner data
}
```

### Action: RETRIEVE PLANNER
### Method: GET
### Endpoint
```bash
{BaseUrlModel}/pk/
```
### Authentication
```bash
Bearer token
```
### Body
```bash
no body
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
{
    ...planner data
}
```
### Action: LIST PLANNER
### Method: GET
### Endpoint
```bash
{BaseUrlModel}/
```
### Authentication
```bash
Bearer token
```
### Body
```bash
no body
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
[
    {
    ...planner data
    },
    {
    ...planner data
    },
    ...
]
```
### Action: PARTIAL UPDATE PLANNER
### Method: PATCH
### Endpoint
```bash
{BaseUrlModel}/pk/
```
### Authentication
```bash
Bearer token
```
### Body  <span style="color: red">[required]</span>
```bash
{
	"free": true,
    ... more fields if necessary
}
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
{
    ... planner data updated
}
```

<p id=user></p>
<h2 style="color: coral">User</h2>
<a href=#summary>Voltar ao topo</a>

### baseUrl model:
```bash
{BaseUrl}/user/
```

## Fields:
```bash
    email = String
    phone = String
    type_account = String
    logged = Boolean
    login_erro = PositiveInteger
    username = String
    first_name = String    
```

## Endpoints:
### Token
- `{BaseUrlModel}/`: Endpoint to create user - method post.
- `{BaseUrlModel}/<uuid:id>/`: Endpoint to retrieve data from a user - method get.
- `{BaseUrlModel}/`: Endpoint to collect data from all user - method get.
- `{BaseUrlModel}/<uuid:id>/`: Endpoint used to partial update a user's data - method patch

### Action: CREATE USER
### Method: POST
### Endpoint
```bash
{BaseUrlModel}/
```
### Authentication
```bash
Bearer token
```
### Body  <span style="color: red">[required]</span>
```bash
{
	"email" : "test@positive.com",
    "phone" : "+5586911111111",
    "type_account" : "free",
    "username" : "firstaccountpositive",
    "first_name" : "Rubens",
}
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 201
```
```bash
{
    ...user data
}
```

### Action: RETRIEVE USER
### Method: GET
### Endpoint
```bash
{BaseUrlModel}/pk/
```
### Authentication
```bash
Bearer token
```
### Body
```bash
no body
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
{
    ...user data
}
```
### Action: LIST USER
### Method: GET
### Endpoint
```bash
{BaseUrlModel}/
```
### Authentication
```bash
Bearer token
```
### Body
```bash
no body
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
[
    {
    ...user data
    },
    {
    ...user data
    },
    ...
]
```
### Action: PARTIAL UPDATE USER
### Method: PATCH
### Endpoint
```bash
{BaseUrlModel}/pk/
```
### Authentication
```bash
Bearer token
```
### Body  <span style="color: red">[required]</span>
```bash
{
	"first_name": "Rubens Rodigues",
    ... more fields if necessary
}
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
{
    ... user data updated
}
```

<p id=useranalysis></p>
<h2 style="color: coral">User Analysis</h2>
<a href=#summary>Voltar ao topo</a>

### baseUrl model:
```bash
{BaseUrl}/user_analysis/
```

## Fields:
```bash
    data = DateTime
    user = User id
    love = PositiveInteger
    free = PositiveInteger
    forgive = PositiveInteger
    spiritualize = PositiveInteger
    undertake = PositiveInteger
    innovate = PositiveInteger
    move = PositiveInteger
    transforme = PositiveInteger
    meditate = PositiveInteger
    take_selfresponsabbility = PositiveInteger
    organize = PositiveInteger
    celebrate = PositiveInteger
    
```

## Endpoints:
### Token
- `{BaseUrlModel}/`: Endpoint to create user analysis - method post.
- `{BaseUrlModel}/<uuid:id>/`: Endpoint to retrieve data from a user analysis - method get.
- `{BaseUrlModel}/`: Endpoint to collect data from all user analysis - method get.
- `{BaseUrlModel}/<uuid:id>/`: Endpoint used to partial update a user analysis's data - method patch

### Action: CREATE USER ANALYSIS
### Method: POST
### Endpoint
```bash
{BaseUrlModel}/
```
### Authentication
```bash
Bearer token
```
### Body  <span style="color: red">[required]</span>
```bash
{
	"data" : "2024-09-21",
    "user" : User id,
    "love" : 10,
    "free" : 10,
    "forgive" : 10,
    "spiritualize" : 10,
    "undertake" : 10,
    "innovate" : 10,
    "move" : 10,
    "transforme" : 10,
    "meditate" : 10,
    "take_selfresponsabbility" : 10,
    "organize" : 10,
    "celebrate" : 9,
}
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 201
```
```bash
{
    ...user analysis data
}
```

### Action: RETRIEVE USER ANALYSIS
### Method: GET
### Endpoint
```bash
{BaseUrlModel}/pk/
```
### Authentication
```bash
Bearer token
```
### Body
```bash
no body
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
{
    ...user analysis data
}
```
### Action: LIST USER ANALYSIS
### Method: GET
### Endpoint
```bash
{BaseUrlModel}/
```
### Authentication
```bash
Bearer token
```
### Body
```bash
no body
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
[
    {
    ...user analysis data
    },
    {
    ...user analysis data
    },
    ...
]
```
### Action: PARTIAL UPDATE USER ANALYSIS
### Method: PATCH
### Endpoint
```bash
{BaseUrlModel}/pk/
```
### Authentication
```bash
Bearer token
```
### Body  <span style="color: red">[required]</span>
```bash
{
	"celebrate" : 10,
    ... more fields if necessary
}
```
### Responses
<p style="font-weight: 900"> Success </p>

```bash
Status code - 200
```
```bash
{
    ... user analysis data updated
}
```
