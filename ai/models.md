# Model Notes

| Use case | Good default | Notes |
| --- | --- | --- |
| Fast Q&A | Small/mini general model | Optimize for latency and cost. |
| Code assistance | Strong reasoning/coding model | Verify with tests and real execution. |
| Summarization | Long-context model | Preserve citations and source links. |
| Local/private demos | Quantized open model | Trade quality for control and offline use. |

## Evaluation checklist

- Accuracy on the actual task
- Latency and throughput
- Cost per useful answer
- Data handling/privacy constraints
- Tool-use and structured-output support
