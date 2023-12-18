# Memo writer

Generate a company memo based on provided points.

- See [https://platform.openai.com/examples/default-memo-writer](https://platform.openai.com/examples/default-memo-writer)
- [Open in OpenAI Playground](https://platform.openai.com/playground/p/default-memo-writer)

## Example Usage

```console
curl --location --request PUT 'https://api.openai.lawrencemcdaniel.com/examples/default-memo-writer' \
--header 'x-api-key: YOUR-API-GATEWAY-KEY' \
--header 'Content-Type: application/json' \
--data '{"Draft a company memo to be distributed to all employees. The memo should cover the following specific points without deviating from the topics mentioned and not writing any fact which is not present here:

Introduction: Remind employees about the upcoming quarterly review scheduled for the last week of April.

Performance Metrics: Clearly state the three key performance indicators (KPIs) that will be assessed during the review: sales targets, customer satisfaction (measured by net promoter score), and process efficiency (measured by average project completion time).

Project Updates: Provide a brief update on the status of the three ongoing company projects:

a. Project Alpha: 75% complete, expected completion by May 30th.
b. Project Beta: 50% complete, expected completion by June 15th.
c. Project Gamma: 30% complete, expected completion by July 31st.

Team Recognition: Announce that the Sales Team was the top-performing team of the past quarter and congratulate them for achieving 120% of their target.

Training Opportunities: Inform employees about the upcoming training workshops that will be held in May, including "Advanced Customer Service" on May 10th and "Project Management Essentials" on May 25th."}'
```

## Example results

```json

```

## Official Documentation

![OpenAI Playground](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/img/examples/example-22-memo-writer.png "OpenAI Playground")
