# RembgAI cURL example
To test the API, just run this simple command.
```
curl -X POST \
    -H "X-RapidAPI-Key: <YOUR_API_KEY>" \
    -H "X-RapidAPI-Host: image-background-removal4.p.rapidapi.com" \
    -f https://image-background-removal4.p.rapidapi.com/remove \
    --data-binary @/absolute/path/to/image.jpg \
    -o output.png
```