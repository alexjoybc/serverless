import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')


    try:
        req_body = req.get_json()
        issue = req_body.get("issue")

        print(issue)

        smsbodyTemplate = "Issue #{}: {}\n is {} on [{}] by {}: \n{} "
    
        smsBody = smsbodyTemplate.format(\
            req_body.get("issue").get("number"),\
            req_body.get("issue").get("title"),\
            req_body.get("issue").get("state"),\
            req_body.get("repository").get("name"),\
            req_body.get("issue").get("user").get("login"),\
            req_body.get("issue").get("html_url"))

        print(smsBody)

        return func.HttpResponse(
            smsBody,
            status_code=200
        )

    except ValueError:
        pass

    return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200
    )
