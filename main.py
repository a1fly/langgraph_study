from langgraph.graph import START,END,StateGraph
from typing_extensions import TypedDict


class mystate(TypedDict):
    name:str
    message:str

def say(state):
      return {
          "message": f"{state['message']} hello {state['name']}"
      }

buider=StateGraph(mystate)
buider.add_node("say",say)
buider.add_edge(START,"say")
buider.add_edge("say",END)


graph=buider.compile()

result=graph.invoke({
    "name":"amy",
    "message":"asdas"
})

print(result)



