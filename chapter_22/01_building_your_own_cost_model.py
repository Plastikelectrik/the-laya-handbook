# The LAYA Handbook — Chapter 22: Cost Modeling: Laya vs. Rules vs. LLM Calls
# Section: Building Your Own Cost Model

def cost_per_decision_llm(price_per_1k_input_tokens, price_per_1k_output_tokens,
                          avg_input_tokens, avg_output_tokens):
    return (avg_input_tokens / 1000) * price_per_1k_input_tokens + \
           (avg_output_tokens / 1000) * price_per_1k_output_tokens

def cost_per_decision_laya(gpu_hourly_cost, measured_throughput_per_second):
    decisions_per_hour = measured_throughput_per_second * 3600
    return gpu_hourly_cost / decisions_per_hour

# Plug in YOUR OWN measured numbers from Chapter 15's exercises and your
# actual provider's published pricing before trusting either result.
