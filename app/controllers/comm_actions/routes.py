import logging

from flask import Blueprint, request, g, jsonify
from flask_pydantic import validate
from pydantic import validator

from app.pydantic_base_model import BaseModel
from app.utils.inflate import inflate

logger = logging.getLogger(__name__)


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


comm_actions_blueprint = Blueprint("comm_actions", __name__)


@comm_actions_blueprint.route("/v3/comm-actions", methods=["POST"])
@inflate
@validate(body=CreateCommActionsBody)
def post(body):
    return jsonify({"status": "success"})
