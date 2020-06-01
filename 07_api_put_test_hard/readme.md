# 06 Test the POST blogger functionality using the provided API documentation.

### API DOCS:

1. http://35.225.243.133/api-documentation/
2. http://35.225.243.133/redoc/




### Test Case 1:
url: http://35.225.243.133/bloggers/
POST VALID DATA:
```
{
    full_name: "Idris Shabanli"
}
```
Expected status code: 201
Expected response:
```
{
    id:	integer
    full_name:	"Idris Shabanli"
    created_at	($date-time)
    updated_at ($date-time)
}
```

1. Check Status code is `201`
2. Check `full_name` is `"Idris Shabanli"` from response


### Test Case 2:
url: http://35.225.243.133/bloggers/
POST INVALID DATA:
```
{
    full_name: "abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd "
}
```
Expected status code: 400
Expected response:
```
{
  "full_name": ["Ensure this field has no more than 180 characters."]
}

```

1. Check Status code is `400`
2. Check `full_name` is `["Ensure this field has no more than 180 characters."]` from response


### Test Case 3:
url: http://35.225.243.133/bloggers/
POST INVALID DATA:
```
{}
```
Expected status code: 400
Expected response:
```
{
  "full_name": ["This field is required."]
}

```

1. Check Status code is `400`
2. Check `full_name` is `["This field is required."]` from response



### Test Case 4:
url: http://35.225.243.133/bloggers/
POST INVALID DATA:
```
{
"id": 1223
}
```
Expected status code: 400
Expected response:
```
{
  "full_name": ["This field is required."]
}

```

1. Check Status code is `400`
2. Check `full_name` is `["This field is required."]` from response