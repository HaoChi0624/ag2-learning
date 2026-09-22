#import asyncio
#from ag2 import Agent
#from ag2.config import OpenAIConfig

#agent = Agent(
   # "assistant",
  #  prompt="You are a helpful assistant.",
 #   config=OpenAIConfig("gpt-4o-mini"),
#)

#async def main() -> None:
#    reply = await agent.ask("Give me one sentence about AG2.")
#    print(reply.body)

#asyncio.run(main())

#async def main() -> None:
    #reply = await agent.ask("Give me one sentence about AG2.")
   # print(reply.body)
  #  follow_up = await reply.ask("Now make it shorter.")
 #   print(follow_up.body)
#asyncio.run(main())
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import asyncio
from ag2 import Agent, tool
from ag2.config import OpenAIConfig

@tool
async def get_weather(city: str) -> str:
    """Return the current weather for a city."""
    return f"It's sunny in {city}."

agent = Agent(
    "assistant",
    prompt="Use tools when helpful.",
    config=OpenAIConfig("gpt-4o-mini"),
    tools=[get_weather],
)

async def main() -> None:
    reply = await agent.ask("What's the weather in Paris?")
    print(reply.body)

asyncio.run(main())