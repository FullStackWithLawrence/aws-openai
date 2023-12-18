# Pro and con discusser

Analyze the pros and cons of a given topic.

- See [https://platform.openai.com/examples/default-pro-con-discusser](https://platform.openai.com/examples/default-pro-con-discusser)
- [Open in OpenAI Playground](https://platform.openai.com/playground/p/default-pro-con-discusser)

## Example Usage

```console
curl --location --request PUT 'https://api.openai.lawrencemcdaniel.com/examples/default-pro-con-discusser' \
--header 'x-api-key: YOUR-API-GATEWAY-KEY' \
--header 'Content-Type: application/json' \
--data '{"Analyze the pros and cons of remote work vs. office work"}'
```

## Example results

```json
{
  "isBase64Encoded": false,
  "statusCode": 200,
  "headers": {
    "Content-Type": "application/json"
  },
  "body": {
    "id": "chatcmpl-7yUJSDimzpH4zH9CxJAqjMhnlYU6T",
    "object": "chat.completion",
    "created": 1694650558,
    "model": "gpt-4-0613",
    "choices": [
      {
        "index": 0,
        "message": {
          "role": "assistant",
          "content": "Remote Work: \n\nPros:\n1. Flexible hours: Remote workers often have the flexibility to set their own schedules, allowing them to balance work and personal life more effectively.\n2. No commute: This saves time and money on transportation and can increase work-life balance.\n3. Custom work environment: Employees can set up their work environment to fit personal preferences.\n4. Global job opportunities: Allows employees to work for any company regardless of the location.\n\nCons:\n1. Isolation: There can be a lack of human interaction, potentially leading to feelings of isolation or loneliness.\n2. Difficulty separating work from home: Some remote workers struggle to distinguish between their work and personal life, potentially leading to burnout.\n3. Less team building: There are fewer opportunities for team-building activities and face-to-face interactions.\n4. Varying productivity: Some people can find it difficult to stay focused without the structure of a traditional office environment.\n\nOffice Work:\n\nPros:\n1. Clear work-life balance: Having a separate place for work can make it easier to disconnect at the end of the day.\n2. Opportunities for collaboration: Physical proximity to coworkers can often make collaboration, brainstorming, and problem-solving easier.\n3. Direct management: Immediate access to supervision or support from managers or colleagues.\n4. Structured environment: A set of standard work hours and traditional professional setup that keeps the focus on the tasks.\n\nCons:\n1. Commuting: Travelling to and from work can be a significant time commitment and can add to daily stress.\n2. Rigidity: The structure of a traditional 9-5 office job can make it harder for employees to balance personal responsibilities.\n3. Limited geographic scope: Office jobs typically require living close to the office location.\n4. Distractions: From impromptu meetings to a noisy coworker, office jobs come with their own set of potential distractions."
        },
        "finish_reason": "stop"
      }
    ],
    "usage": {
      "prompt_tokens": 24,
      "completion_tokens": 378,
      "total_tokens": 402
    }
  }
}
```

## Official Documentation

![OpenAI Playground](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/img/examples/example-29-pro-con-discusser.png "OpenAI Playground")
