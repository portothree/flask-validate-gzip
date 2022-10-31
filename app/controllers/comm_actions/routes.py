import logging

from flask import Blueprint, request, g, jsonify
from flask.views import MethodView
from flask_pydantic import validate
from pydantic import validator

from app.pydantic_base_model import BaseModel
from app.utils.inflate import inflate

logger = logging.getLogger(__name__)


class JSONView(MethodView):
    def validate_request(self):
        if not request.mimetype == "application/json":
            raise BadRequest(description=f"Invalid MimeType: {request.mimetype}")
        return True

class CreateCommActionsBodyRaw(BaseModel):
    run_id: str

class CreateCommActionsBody(CreateCommActionsBodyRaw):
    @validator("run_id")
    def validate_run_id(cls, v):
        """
        Validate that the run_id field is a string
        """
        if not isinstance(v, str):
            raise ValueError("run_id must be a string")
        return v


class CommActionsView(JSONView):
    @inflate
    @validate(body=CreateCommActionsBody)
    def post(body):
        print(body)

        return jsonify({"status": "success"})


def get_comm_actions_blueprint():
    comm_actions_blueprint = Blueprint("comm_actions", __name__)
    comm_actions_blueprint.add_url_rule(
        "/v3/comm-actions", view_func=CommActionsView().as_view("v3_comm_actions")
    )

    return comm_actions_blueprint


comm_actions_blueprint = get_comm_actions_blueprint()
