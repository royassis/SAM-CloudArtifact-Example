FROM public.ecr.aws/lambda/python:3.9

COPY requirements.txt .

ARG mydomain
ARG myrepo
ARG accountid
ARG CODEARTIFACT_AUTH_TOKEN

ARG INDEX_URL="https://aws:$CODEARTIFACT_AUTH_TOKEN@$mydomain-$accountid.d.codeartifact.us-east-1.amazonaws.com/pypi/$myrepo/simple/"
RUN  pip3 install requester-commons --target "${LAMBDA_TASK_ROOT}" --index-url $INDEX_URL --upgrade --root-user-action=ignore
    
COPY . ${LAMBDA_TASK_ROOT}
    
CMD [ "app.handler" ]
