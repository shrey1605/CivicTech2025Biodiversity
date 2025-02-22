from fastapi import FastAPI, UploadFile
import uvicorn
from llm import get_sub_species_info_from_LLM

app = FastAPI()


# routes
@app.get("/hello")
def hello(name: str = ""):
    return {"message": f"Hello, this is our civic tech project"}

# expecting the following json doc
# {
#     location: "Boston"
# }
@app.post("/getInfo/")
async def getInfo():
    # Get all the info for genuses/all that shit for that location from
    # the herbarium dataset csv file

    # we basically assign random occurrence values for each genus/sub-genus we get

    # Now, we have a list of genus/sub-genus. Pick the top 5, then use any LLM AI API
    # get all the information about that. pack it in to the json object
    # textOfThatSubSpecies = get_sub_species_info_from_LLM(sub_species_name)

    # return that object
    


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)




# The flow goes like
# first we perform ocr on the given image
# we get all the text in that image from that OCR analysis. We also get bounding box data
# we then send this text to some LLM to extract words worth listing meaning for
# we get a list of words and their meanings back from that LLM
# Now we use oxford and other reliable dictionaries to get word meanings
# we then package all this together and send it to the front-end