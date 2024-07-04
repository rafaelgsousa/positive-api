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

<p id=albummeeting></p>
<h2 style="color: green">Album Meeting</h2>
<a href=#summary>Voltar ao topo</a>

### baseUrl model:
```bash
{BaseUrl}/album_meeting/
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
- `{BaseUrlModel}/`: Endpoint to create album meeting - method post.
- `{BaseUrlModel}/<uuid:id>/`: Endpoint to retrieve data from a album meeting - method get.
- `{BaseUrlModel}/`: Endpoint to collect data from all album meetings - method get.
- `{BaseUrlModel}/<uuid:id>/`: Endpoint used to partial update a album meeting's data - method patch.

<p id=imagealbummeeting></p>
<h2 style="color: green">Image Album Meeting</h2>
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
```

## Endpoints:
### Token
- `{BaseUrlModel}/`: Endpoint to create image album meeting - method post.
- `{BaseUrlModel}/<uuid:id>/`: Endpoint to retrieve data from a image album meeting - method get.
- `{BaseUrlModel}/`: Endpoint to collect data from all image album meetings - method get.
- `{BaseUrlModel}/<uuid:id>/`: Endpoint used to partial update a image album meeting's data - method patch.

<p id=videomeeting></p>
<h2 style="color: green">Video Meeting</h2>
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
```

## Endpoints:
### Token
- `{BaseUrlModel}/`: Endpoint to create video meeting - method post.
- `{BaseUrlModel}/<uuid:id>/`: Endpoint to retrieve data from a video meeting - method get.
- `{BaseUrlModel}/`: Endpoint to collect data from all video meetings - method get.
- `{BaseUrlModel}/<uuid:id>/`: Endpoint used to partial update a video meeting's data - method patch