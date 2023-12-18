# Single page website creator

Create a single page website.

- See [https://platform.openai.com/examples/default-single-page-website](https://platform.openai.com/examples/default-single-page-website)
- [Open in OpenAI Playground](https://platform.openai.com/playground/p/default-single-page-website)

## Example Usage

```console
curl --location --request PUT 'https://api.openai.lawrencemcdaniel.com/examples/default-single-page-website' \
--header 'x-api-key: YOUR-API-GATEWAY-KEY' \
--header 'Content-Type: application/json' \
--data '{"Make a single page website that shows off different neat javascript features for drop-downs and things to display information. The website should be an HTML file with embedded javascript and CSS."}'
```

## Example results

````json
{
  "retval": {
    "isBase64Encoded": false,
    "statusCode": 200,
    "headers": {
      "Content-Type": "application/json"
    },
    "body": {
      "id": "chatcmpl-7yUl2CBzp93yjsudcr3OffoTI3Th4",
      "object": "chat.completion",
      "created": 1694652268,
      "model": "gpt-4-0613",
      "choices": [
        {
          "index": 0,
          "message": {
            "role": "assistant",
            "content": "Here's a simple HTML file that includes a dropdown menu with JavaScript event handlers and a toggleable information box.\n\n```html\n<!DOCTYPE html>\n<html>\n<head>\n    <style>\n        body {\n            font-family: Arial, sans-serif;\n        }\n\n        #infoBox {\n            display: none;\n            border: 1px solid #ccc;\n            padding: 10px;\n            margin-top: 10px;\n            width: 200px;\n        }\n    </style>\n</head>\n<body>\n\n    <h2>JavaScript Drop-down Menu</h2>\n\n    <label for=\"choices\">Choose a piece of information:</label>\n    <select id=\"choices\" onchange=\"displayInfo(this.value)\">\n        <option value=\"0\">Select...</option>\n        <option value=\"1\">Fact 1</option>\n        <option value=\"2\">Fact 2</option>\n        <option value=\"3\">Fact 3</option>\n    </select>\n\n    <div id=\"infoBox\"></div>\n\n    <script>\n        const facts = [\n            '',\n            'Fact 1: JavaScript is the language of the web.',\n            'Fact 2: JavaScript and Java are not the same thing.',\n            'Fact 3: JavaScript allows to create interactive web pages.'\n        ];\n\n        function displayInfo(value) {\n            const infoBox = document.getElementById(\"infoBox\");\n            infoBox.style.display = \"block\";\n            infoBox.innerHTML = facts[value];\n        }\n    </script>\n\n</body>\n</html>\n```\nThis page contains a dropdown menu, which has an `onchange` event handler attached. Whenever the selected option is changed, it calls the `displayInfo` function, which changes the inner HTML of the `#infoBox` div to display the selected fact.\n\nThe CSS in the `<head>` part of this HTML document styles the information box, hiding it when it has no content, and providing it with a border, some padding, and a top margin when it displays some information."
          },
          "finish_reason": "stop"
        }
      ],
      "usage": {
        "prompt_tokens": 46,
        "completion_tokens": 413,
        "total_tokens": 459
      }
    }
  }
}
````

## Official Documentation

![OpenAI Playground](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/img/examples/example-20-single-page-website.png "OpenAI Playground")
