import requests
from django.http import JsonResponse
from django.shortcuts import render
# Example code for error handling in fetch_data_from_api
import logging
import requests

logger = logging.getLogger(__name__)

def fetch_data_from_api():
    try:
        url = "https://devapi.beyondchats.com/api/get_message_with_sources"
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for bad responses
        data = response.json()
        logger.info("Data fetched successfully from API.")
        return data
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching data from API: {e}")
        raise
    except ValueError as e:
        logger.error(f"Error decoding JSON data: {e}")
        raise




def identify_citations(data):
    citations = []
    
    # Check for expected keys and structure
    if 'data' in data and isinstance(data['data'], list):
        for item in data['data']:
            if 'response' in item and 'sources' in item:
                response_text = item['response']
                sources = item['sources']
                cited_sources = []
                for source in sources:
                    # Check if the source context is mentioned in the response text
                    if 'context' in source and source['context'].lower() in response_text.lower():
                        cited_sources.append({
                            "id": source['id'],
                            "link": source.get('link', '')  # Get the link if available
                        })
                citations.extend(cited_sources)
            else:
                print("Error: Missing response or sources key in item:", item)
    else:
        print("Error: Unexpected data structure", data)
    
    return citations






from django.http import JsonResponse
import requests

def get_citations(request):
    try:
        data = fetch_data_from_api()
        citations = identify_citations(data)
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": str(e)}, status=500)
    except KeyError as e:
        return JsonResponse({"error": f"Key error: {str(e)}"}, status=500)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    
    return JsonResponse(citations, safe=False)




def citations_view(request):
    return render(request, 'citations.html')
