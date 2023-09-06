# Source
# https://www.land.vic.gov.au/land-registration/fees-guides-and-forms/transfer-of-land-fees-calculator

from enum import Enum
import math

class Era(Enum):
    _2023_2024 = 4
    _2022_2023 = 3
    _2021_2022 = 2
    _2020_2021 = 1

class LodgementType(Enum):
    PAPER = 1
    ELECTRONIC = 2

FEES = {
    Era._2023_2024: {
        "paper_lodgement": 105.70,
        "electronic_lodgement": 96.00,
        "consideration_factor": 2.34,
        "easement_fee": 560.20,
        "max_paper": 3616,
        "max_electronic": 3607
    },
    Era._2022_2023: {
        "paper_lodgement": 101.70,
        "electronic_lodgement": 92.40,
        "consideration_factor": 2.34,
        "easement_fee": 538.60,
        "max_paper": 3612,
        "max_electronic": 3603
    },
    Era._2021_2022: {
        "paper_lodgement": 99.90,
        "electronic_lodgement": 90.80,
        "consideration_factor": 2.34,
        "easement_fee": 529.50,
        "max_paper": 3610,
        "max_electronic": 3601
    },
    Era._2020_2021: {
        "paper_lodgement": 98.50,
        "electronic_lodgement": 89.50,
        "consideration_factor": 2.34,
        "easement_fee": 521.70,
        "max_paper": 3609,
        "max_electronic": 3600
    },
}

def calculate_land_transfer_fees(consideration: float, lodgement_type: LodgementType, easement_created_or_surrendered: bool, era: Era=Era._2023_2024) -> float:
    """Calculate land transfer fees for Victoria
    """
    paper_lodgement_fee = FEES[era]["paper_lodgement"]
    electronic_lodgement_fee = FEES[era]["electronic_lodgement"]
    consideration_factor = FEES[era]["consideration_factor"]
    easement_fee = FEES[era]["easement_fee"]
    max_paper = FEES[era]["max_paper"]
    max_electronic = FEES[era]["max_electronic"]
    fee = 0
    max_fee = 0
    if lodgement_type == LodgementType.PAPER:
            fee += paper_lodgement_fee
            max_fee = max_paper
    elif lodgement_type == LodgementType.ELECTRONIC:
            fee += electronic_lodgement_fee
            max_fee = max_electronic
    else:
            raise ValueError("Unexpected value in lodgement_type")
    if easement_created_or_surrendered:
        fee += easement_fee
    if consideration >= 1000:
        fee += math.floor(consideration / 1000) * consideration_factor
        fee = min(fee, round(max_fee))
    if (easement_created_or_surrendered and consideration < 1000) or consideration >= 1000:
        fee = math.ceil(fee)
    return fee
