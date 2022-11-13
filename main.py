import json
import modelDriver
import api
#Run source ./python/bin/activate to activate the virtual environment
if __name__ == '__main__':
    api.app.run(debug=True)

# def lambda_handler(event, context):
#     event = json.loads(event['body'])
#     #(event)
    
#     reqType = ''
#     try:
#         reqType = event['Request Type']
#     except:
#         return json.dumps("Invalid input format. Make sure there is a 'Request Type' field")
#     if reqType is None:
#         return json.dumps("Invalid input format. Make sure there is a 'Request Type' field")
#     try:
#         if reqType == 'Echo':
#             return json.dumps(event)
#         elif reqType == 'Songify Page':
#             mod = event['Model']
#             if type(mod) is not int:
#                 return json.dumps("Invalid input format. Make sure there is a 'Model' field that is an integer")
#             data = event['Data']
#             if type(data) is not str:
#                 return json.dumps("Invalid input format. Make sure there is a 'Data' field that is a string")
#             if (mod == 1):
#                 songs = []
#                 artists = []
#                 albums = []
#                 predictions = modelDriver.predictModel("./models/SAA.spacy", "./models/outputs/output.txt", data)
#                 for i in range(len(predictions)):
#                     if predictions[i][1] == 'Song':
#                         songs.append(predictions[i][2])
#                     elif predictions[i][1] == 'Artist':
#                         artists.append(predictions[i][2])
#                     elif predictions[i][1] == 'Album':
#                         albums.append(predictions[i][2])
#                 toRet = {
#                     "Songs": songs,
#                     "Artists": artists,
#                     "Albums": albums
#                 }
#                 return json.dumps(toRet) #Returns an array of the predicted labels.
#             else:
#                 return json.dumps("Invalid Model")
#     except Exception as e:
#         return json.dumps("Something went wrong somewhere. Exception: " + str(e))
#     return {
#         'statusCode': 200,
#         'body': json.dumps('Hello from Lambda!')
# }