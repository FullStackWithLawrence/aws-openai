# Function from specification

Create a Python function from a specification.

- See [https://platform.openai.com/examples/default-function-from-spec](https://platform.openai.com/examples/default-function-from-spec)
- [Open in OpenAI Playground](https://platform.openai.com/playground/p/default-function-from-spec)

## Example Usage

```console
curl --location --request PUT 'https://api.openai.lawrencemcdaniel.com/examples/default-function-from-spec' \
--header 'x-api-key: YOUR-API-GATEWAY-KEY' \
--header 'Content-Type: application/json' \
--data '{"Write a Python function that takes as input a file path to an image, loads the image into memory as a numpy array, then crops the rows and columns around the perimeter if they are darker than a threshold value. Use the mean value of rows and columns to decide if they should be marked for deletion."}'
```

## Example results

````json
{
  "isBase64Encoded": false,
  "statusCode": 200,
  "headers": {
    "Content-Type": "application/json"
  },
  "body": {
    "id": "chatcmpl-7yU3zxScvzbhF2jINgJCbSVKAByut",
    "object": "chat.completion",
    "created": 1694649599,
    "model": "gpt-4-0613",
    "choices": [
      {
        "index": 0,
        "message": {
          "role": "assistant",
          "content": "To implement this, we are going to use the OpenCV and Numpy libraries. Here is a possible implementation of the function you asked for:\n\n```python\nimport cv2\nimport numpy as np\n\ndef crop_dark_areas(image_path, threshold):\n    # Load the image into a numpy array\n    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)\n\n    # Compute the mean value for each row and column\n    avg_rows = np.average(img, axis=1)\n    avg_cols = np.average(img, axis=0)\n\n    # Find the indices of rows and columns to keep\n    rows_to_keep = np.where(avg_rows > threshold)[0]\n    cols_to_keep = np.where(avg_cols > threshold)[0]\n\n    # Crop the rows and columns\n    img_cropped = img[np.min(rows_to_keep):np.max(rows_to_keep)+1, np.min(cols_to_keep):np.max(cols_to_keep)+1]\n\n    return img_cropped\n```\n\nThis function works by first loading the image into a Numpy array with grayscale values. Then, it computes the mean value of every row and every column in the image, and decides whether to keep a row or a column based on whether its mean value is greater than the given threshold.\n\nPlease make sure to have OpenCV and numpy installed in your python environment. If not installed, please use the following commands to install:\n- OpenCV: `pip install opencv-python`\n- Numpy: `pip install numpy`"
        },
        "finish_reason": "stop"
      }
    ],
    "usage": {
      "prompt_tokens": 72,
      "completion_tokens": 306,
      "total_tokens": 378
    }
  }
}
````

## Official Documentation

![OpenAI Playground](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/img/examples/example-18-function-from-spec.png "OpenAI Playground")
