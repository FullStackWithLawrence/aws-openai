# Rap battle writer

Generate a rap battle between two characters.

- See [https://platform.openai.com/examples/default-rap-battle](https://platform.openai.com/examples/default-rap-battle)
- [Open in OpenAI Playground](https://platform.openai.com/playground/p/default-rap-battle)

## Example Usage

```console
curl --location --request PUT 'https://api.openai.lawrencemcdaniel.com/examples/default-rap-battle' \
--header 'x-api-key: YOUR-API-GATEWAY-KEY' \
--header 'Content-Type: application/json' \
--data '{"Write a rap battle between Alan Turing and Claude Shannon."}'
```

## Example results

```json
{
  "retval": {
    "isBase64Encoded": false,
    "statusCode": 200,
    "headers": {
      "Content-Type": "application/json"
    },
    "body": {
      "id": "chatcmpl-7yUlc4YOZIA8z2QWUimt3UAs48ELf",
      "object": "chat.completion",
      "created": 1694652304,
      "model": "gpt-4-0613",
      "choices": [
        {
          "index": 0,
          "message": {
            "role": "assistant",
            "content": "Verse 1 - Alan Turing:\n\nTuring's the name, I'm the game changer,\nAI's genesis, its potential engager.\nBroke the Enigma, won the world-wide war,\nDid in years what would've taken four-score.\n\nClaude Shannon, yeah, I heard of you,\nYour information theory is cool and new,\nBut without my machine, where would you be?\nStill fumbling with uncertainty?\n\nVerse 2 - Claude Shannon:\n\nClaude Shannon here, master of communication,\nLaid the foundation for the tech innovation.\nFrom entropy to redundancy, I made it clear,\nWithout me, you wouldn’t be here.\n\nTuring, you're a scholar, and your creation's legit,\nBut you needed my circuits to make it all fit.\nWithout my binary, your machine would be moot,\nI'm the rhythm to your computability flute.\n\nVerse 3 - Alan Turing:\n\nI’m the father of computers, gave silicon life,\nYour theories are nice, but I cut through like a knife.\nI built from scratch, made thought transmissible,\nMy Turing Test made the impossible feasible.\n\nYes, your binary helped, won't deny it's true,\nBut remember, the machine's architecture is due.\nTo me, your contribution's just a part of,\nThe grand machine I brought forth as an art.\n\nVerse 4 - Claude Shannon:\n\nYou created AI, and I’ll give you your due,\nBut my digital circuits gave its life it's true hue.\nYes, your creation’s great, made the world look bright,\nBut my information theory gave it flight.\n\nSure, your tests were nice, and they made a splash,\nBut my foundations turned that splash into cash.\nSo here’s to us, Turing, it’s no contest,\nWhen it comes to pioneers, we’re simply the best."
          },
          "finish_reason": "stop"
        }
      ],
      "usage": {
        "prompt_tokens": 22,
        "completion_tokens": 366,
        "total_tokens": 388
      }
    }
  }
}
```

## Official Documentation

![OpenAI Playground](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/img/examples/example-21-rap-battle.png "OpenAI Playground")
