# generated by datamodel-codegen:
#   filename:  marketplace_plans.csv
#   timestamp: 2025-07-04T16:56:56+00:00

from __future__ import annotations

from typing import List, Optional, Union
from pydantic import BaseModel, Field, RootModel
from typing import List, Optional


class MarketplacePlanCSV(BaseModel):
    State_Code: str = Field(..., alias='State Code')
    FIPS_County_Code: str = Field(..., alias='FIPS County Code')
    County_Name: str = Field(..., alias='County Name')
    Metal_Level: str = Field(..., alias='Metal Level')
    Issuer_Name: str = Field(..., alias='Issuer Name')
    HIOS_Issuer_ID: str = Field(..., alias='HIOS Issuer ID')
    Plan_ID__Standard_Component_: str = Field(..., alias='Plan ID (Standard Component)')
    Plan_Marketing_Name: str = Field(..., alias='Plan Marketing Name')
    Standardized_Plan_Option: str = Field(..., alias='Standardized Plan Option')
    Plan_Type: str = Field(..., alias='Plan Type')
    Rating_Area: str = Field(..., alias='Rating Area')
    Child_Only_Offering: str = Field(..., alias='Child Only Offering')
    Source: str
    Customer_Service_Phone_Number_Local: str = Field(
        ..., alias='Customer Service Phone Number Local'
    )
    Customer_Service_Phone_Number_Toll_Free: str = Field(
        ..., alias='Customer Service Phone Number Toll Free'
    )
    Customer_Service_Phone_Number_TTY: str = Field(
        ..., alias='Customer Service Phone Number TTY'
    )
    Network_URL: str = Field(..., alias='Network URL')
    Plan_Brochure_URL: str = Field(..., alias='Plan Brochure URL')
    Summary_of_Benefits_URL: str = Field(..., alias='Summary of Benefits URL')
    Drug_Formulary_URL: str = Field(..., alias='Drug Formulary URL')
    Adult_Dental_: str = Field(..., alias='Adult Dental ')
    Child_Dental_: str = Field(..., alias='Child Dental ')
    EHB_Percent_of_Total_Premium: str = Field(..., alias='EHB Percent of Total Premium')
    Premium_Child_Age_0_14: str = Field(..., alias='Premium Child Age 0-14')
    Premium_Child_Age_18: str = Field(..., alias='Premium Child Age 18')
    Premium_Adult_Individual_Age_21: str = Field(
        ..., alias='Premium Adult Individual Age 21'
    )
    Premium_Adult_Individual_Age_27: str = Field(
        ..., alias='Premium Adult Individual Age 27'
    )
    Premium_Adult_Individual_Age_30_: str = Field(
        ..., alias='Premium Adult Individual Age 30 '
    )
    Premium_Adult_Individual_Age_40_: str = Field(
        ..., alias='Premium Adult Individual Age 40 '
    )
    Premium_Adult_Individual_Age_50_: str = Field(
        ..., alias='Premium Adult Individual Age 50 '
    )
    Premium_Adult_Individual_Age_60_: str = Field(
        ..., alias='Premium Adult Individual Age 60 '
    )
    Premium_Couple_21__: str = Field(..., alias='Premium Couple 21  ')
    Premium_Couple_30_: str = Field(..., alias='Premium Couple 30 ')
    Premium_Couple_40_: str = Field(..., alias='Premium Couple 40 ')
    Premium_Couple_50_: str = Field(..., alias='Premium Couple 50 ')
    Premium_Couple_60_: str = Field(..., alias='Premium Couple 60 ')
    Couple_1_child__Age_21: str = Field(..., alias='Couple+1 child, Age 21')
    Couple_1_child__Age_30_: str = Field(..., alias='Couple+1 child, Age 30 ')
    Couple_1_child__Age_40_: str = Field(..., alias='Couple+1 child, Age 40 ')
    Couple_1_child__Age_50_: str = Field(..., alias='Couple+1 child, Age 50 ')
    Couple_2_children__Age_21: str = Field(..., alias='Couple+2 children, Age 21')
    Couple_2_children__Age_30_: str = Field(..., alias='Couple+2 children, Age 30 ')
    Couple_2_children__Age_40_: str = Field(..., alias='Couple+2 children, Age 40 ')
    Couple_2_children__Age_50: str = Field(..., alias='Couple+2 children, Age 50')
    Couple_3_or_more_Children__Age_21: str = Field(
        ..., alias='Couple+3 or more Children, Age 21'
    )
    Couple_3_or_more_Children__Age_30: str = Field(
        ..., alias='Couple+3 or more Children, Age 30'
    )
    Couple_3_or_more_Children__Age_40: str = Field(
        ..., alias='Couple+3 or more Children, Age 40'
    )
    Couple_3_or_more_Children__Age_50: str = Field(
        ..., alias='Couple+3 or more Children, Age 50'
    )
    Individual_1_child__Age_21: str = Field(..., alias='Individual+1 child, Age 21')
    Individual_1_child__Age_30: str = Field(..., alias='Individual+1 child, Age 30')
    Individual_1_child__Age_40: str = Field(..., alias='Individual+1 child, Age 40')
    Individual_1_child__Age_50: str = Field(..., alias='Individual+1 child, Age 50')
    Individual_2_children__Age_21: str = Field(
        ..., alias='Individual+2 children, Age 21'
    )
    Individual_2_children__Age_30: str = Field(
        ..., alias='Individual+2 children, Age 30'
    )
    Individual_2_children__Age_40: str = Field(
        ..., alias='Individual+2 children, Age 40'
    )
    Individual_2_children__Age_50: str = Field(
        ..., alias='Individual+2 children, Age 50'
    )
    Individual_3_or_more_children__Age_21: str = Field(
        ..., alias='Individual+3 or more children, Age 21'
    )
    Individual_3_or_more_children__Age_30: str = Field(
        ..., alias='Individual+3 or more children, Age 30'
    )
    Individual_3_or_more_children__Age_40: str = Field(
        ..., alias='Individual+3 or more children, Age 40'
    )
    Individual_3_or_more_children__Age_50: str = Field(
        ..., alias='Individual+3 or more children, Age 50'
    )
    Medical_Deductible___Individual___Standard: str = Field(
        ..., alias='Medical Deductible - Individual - Standard'
    )
    Drug_Deductible___Individual___Standard: str = Field(
        ..., alias='Drug Deductible - Individual - Standard'
    )
    Medical_Deductible___Family___Standard: str = Field(
        ..., alias='Medical Deductible - Family - Standard'
    )
    Drug_Deductible___Family___Standard: str = Field(
        ..., alias='Drug Deductible - Family - Standard'
    )
    Medical_Deductible___Family__Per_Person____Standard: str = Field(
        ..., alias='Medical Deductible - Family (Per Person) - Standard'
    )
    Drug_Deductible___Family__Per_Person____Standard: str = Field(
        ..., alias='Drug Deductible - Family (Per Person) - Standard'
    )
    Medical_Maximum_Out_Of_Pocket___Individual___Standard: str = Field(
        ..., alias='Medical Maximum Out Of Pocket - Individual - Standard'
    )
    Drug_Maximum_Out_Of_Pocket___Individual___Standard: str = Field(
        ..., alias='Drug Maximum Out Of Pocket - Individual - Standard'
    )
    Medical_Maximum_Out_Of_Pocket___Family___Standard: str = Field(
        ..., alias='Medical Maximum Out Of Pocket - Family - Standard'
    )
    Drug_Maximum_Out_Of_Pocket___Family___Standard: str = Field(
        ..., alias='Drug Maximum Out Of Pocket - Family - Standard'
    )
    Medical_Maximum_Out_Of_Pocket___Family__Per_Person____Standard: str = Field(
        ..., alias='Medical Maximum Out Of Pocket - Family (Per Person) - Standard'
    )
    Drug_Maximum_Out_Of_Pocket___Family__Per_Person____Standard: str = Field(
        ..., alias='Drug Maximum Out Of Pocket - Family (Per Person) - Standard'
    )
    Primary_Care_Physician___Standard: str = Field(
        ..., alias='Primary Care Physician - Standard'
    )
    Specialist___Standard: str = Field(..., alias='Specialist - Standard')
    Emergency_Room___Standard: str = Field(..., alias='Emergency Room - Standard')
    Inpatient_Facility___Standard: str = Field(
        ..., alias='Inpatient Facility - Standard'
    )
    Inpatient_Physician___Standard: str = Field(
        ..., alias='Inpatient Physician - Standard'
    )
    Generic_Drugs___Standard: str = Field(..., alias='Generic Drugs - Standard')
    Preferred_Brand_Drugs___Standard: str = Field(
        ..., alias='Preferred Brand Drugs - Standard'
    )
    Non_preferred_Brand_Drugs___Standard: str = Field(
        ..., alias='Non-preferred Brand Drugs - Standard'
    )
    Specialty_Drugs___Standard: str = Field(..., alias='Specialty Drugs - Standard')
    field_73_Percent_Actuarial_Value_Silver_Plan_Cost_Sharing: str = Field(
        ..., alias='73 Percent Actuarial Value Silver Plan Cost Sharing'
    )
    Medical_Deductible___Individual___73_Percent: str = Field(
        ..., alias='Medical Deductible - Individual - 73 Percent'
    )
    Drug_Deductible___Individual___73_Percent: str = Field(
        ..., alias='Drug Deductible - Individual - 73 Percent'
    )
    Medical_Deductible___Family___73_Percent: str = Field(
        ..., alias='Medical Deductible - Family - 73 Percent'
    )
    Drug_Deductible___Family___73_Percent: str = Field(
        ..., alias='Drug Deductible - Family - 73 Percent'
    )
    Medical_Deductible___Family__Per_Person____73_Percent: str = Field(
        ..., alias='Medical Deductible - Family (Per Person) - 73 Percent'
    )
    Drug_Deductible___Family__Per_Person____73_Percent: str = Field(
        ..., alias='Drug Deductible - Family (Per Person) - 73 Percent'
    )
    Medical_Maximum_Out_Of_Pocket___Individual___73_Percent: str = Field(
        ..., alias='Medical Maximum Out Of Pocket - Individual - 73 Percent'
    )
    Drug_Maximum_Out_Of_Pocket___Individual___73_Percent: str = Field(
        ..., alias='Drug Maximum Out Of Pocket - Individual - 73 Percent'
    )
    Medical_Maximum_Out_Of_Pocket___Family___73_Percent: str = Field(
        ..., alias='Medical Maximum Out Of Pocket - Family - 73 Percent'
    )
    Drug_Maximum_Out_Of_Pocket___Family___73_Percent: str = Field(
        ..., alias='Drug Maximum Out Of Pocket - Family - 73 Percent'
    )
    Medical_Maximum_Out_Of_Pocket___Family__Per_Person____73_Percent: str = Field(
        ..., alias='Medical Maximum Out Of Pocket - Family (Per Person) - 73 Percent'
    )
    Drug_Maximum_Out_Of_Pocket___Family__Per_Person____73_Percent: str = Field(
        ..., alias='Drug Maximum Out Of Pocket - Family (Per Person) - 73 Percent'
    )
    Primary_Care_Physician___73_Percent: str = Field(
        ..., alias='Primary Care Physician - 73 Percent'
    )
    Specialist___73_Percent: str = Field(..., alias='Specialist - 73 Percent')
    Emergency_Room___73_Percent: str = Field(..., alias='Emergency Room - 73 Percent')
    Inpatient_Facility___73_Percent: str = Field(
        ..., alias='Inpatient Facility - 73 Percent'
    )
    Inpatient_Physician___73_Percent: str = Field(
        ..., alias='Inpatient Physician - 73 Percent'
    )
    Generic_Drugs___73_Percent: str = Field(..., alias='Generic Drugs - 73 Percent')
    Preferred_Brand_Drugs___73_Percent: str = Field(
        ..., alias='Preferred Brand Drugs - 73 Percent'
    )
    Non_preferred_Brand_Drugs___73_Percent: str = Field(
        ..., alias='Non-preferred Brand Drugs - 73 Percent'
    )
    Specialty_Drugs___73_Percent: str = Field(..., alias='Specialty Drugs - 73 Percent')
    field_87_Percent_Actuarial_Value_Silver_Plan_Cost_Sharing: str = Field(
        ..., alias='87 Percent Actuarial Value Silver Plan Cost Sharing'
    )
    Medical_Deductible___Individual___87_Percent: str = Field(
        ..., alias='Medical Deductible - Individual - 87 Percent'
    )
    Drug_Deductible___Individual___87_Percent: str = Field(
        ..., alias='Drug Deductible - Individual - 87 Percent'
    )
    Medical_Deductible___Family___87_Percent: str = Field(
        ..., alias='Medical Deductible - Family - 87 Percent'
    )
    Drug_Deductible___Family___87_Percent: str = Field(
        ..., alias='Drug Deductible - Family - 87 Percent'
    )
    Medical_Deductible___Family__Per_Person____87_Percent: str = Field(
        ..., alias='Medical Deductible - Family (Per Person) - 87 Percent'
    )
    Drug_Deductible___Family__Per_Person____87_Percent: str = Field(
        ..., alias='Drug Deductible - Family (Per Person) - 87 Percent'
    )
    Medical_Maximum_Out_Of_Pocket___Individual___87_Percent: str = Field(
        ..., alias='Medical Maximum Out Of Pocket - Individual - 87 Percent'
    )
    Drug_Maximum_Out_Of_Pocket___Individual___87_Percent: str = Field(
        ..., alias='Drug Maximum Out Of Pocket - Individual - 87 Percent'
    )
    Medical_Maximum_Out_Of_Pocket___Family___87_Percent: str = Field(
        ..., alias='Medical Maximum Out Of Pocket - Family - 87 Percent'
    )
    Drug_Maximum_Out_Of_Pocket___Family___87_Percent: str = Field(
        ..., alias='Drug Maximum Out Of Pocket - Family - 87 Percent'
    )
    Medical_Maximum_Out_Of_Pocket___Family__Per_Person____87_Percent: str = Field(
        ..., alias='Medical Maximum Out Of Pocket - Family (Per Person) - 87 Percent'
    )
    Drug_Maximum_Out_Of_Pocket___Family__Per_Person____87_Percent: str = Field(
        ..., alias='Drug Maximum Out Of Pocket - Family (Per Person) - 87 Percent'
    )
    Primary_Care_Physician___87_Percent: str = Field(
        ..., alias='Primary Care Physician - 87 Percent'
    )
    Specialist___87_Percent: str = Field(..., alias='Specialist - 87 Percent')
    Emergency_Room___87_Percent: str = Field(..., alias='Emergency Room - 87 Percent')
    Inpatient_Facility___87_Percent: str = Field(
        ..., alias='Inpatient Facility - 87 Percent'
    )
    Inpatient_Physician___87_Percent: str = Field(
        ..., alias='Inpatient Physician - 87 Percent'
    )
    Generic_Drugs___87_Percent: str = Field(..., alias='Generic Drugs - 87 Percent')
    Preferred_Brand_Drugs___87_Percent: str = Field(
        ..., alias='Preferred Brand Drugs - 87 Percent'
    )
    Non_preferred_Brand_Drugs___87_Percent: str = Field(
        ..., alias='Non-preferred Brand Drugs - 87 Percent'
    )
    Specialty_Drugs___87_Percent: str = Field(..., alias='Specialty Drugs - 87 Percent')
    field_94_Percent_Actuarial_Value_Silver_Plan_Cost_Sharing: str = Field(
        ..., alias='94 Percent Actuarial Value Silver Plan Cost Sharing'
    )
    Medical_Deductible___Individual___94_Percent: str = Field(
        ..., alias='Medical Deductible - Individual - 94 Percent'
    )
    Drug_Deductible___Individual___94_Percent: str = Field(
        ..., alias='Drug Deductible - Individual - 94 Percent'
    )
    Medical_Deductible___Family___94_Percent: str = Field(
        ..., alias='Medical Deductible - Family - 94 Percent'
    )
    Drug_Deductible___Family___94_Percent: str = Field(
        ..., alias='Drug Deductible - Family - 94 Percent'
    )
    Medical_Deductible___Family__Per_Person____94_Percent: str = Field(
        ..., alias='Medical Deductible - Family (Per Person) - 94 Percent'
    )
    Drug_Deductible___Family__Per_Person____94_Percent: str = Field(
        ..., alias='Drug Deductible - Family (Per Person) - 94 Percent'
    )
    Medical_Maximum_Out_Of_Pocket__individual___94_Percent: str = Field(
        ..., alias='Medical Maximum Out Of Pocket -individual - 94 Percent'
    )
    Drug_Maximum_Out_Of_Pocket___individual___94_Percent: str = Field(
        ..., alias='Drug Maximum Out Of Pocket - individual - 94 Percent'
    )
    Medical_Maximum_Out_Of_Pocket___family___94_Percent: str = Field(
        ..., alias='Medical Maximum Out Of Pocket - family - 94 Percent'
    )
    Drug_Maximum_Out_Of_Pocket___Family____94_Percent: str = Field(
        ..., alias='Drug Maximum Out Of Pocket - Family  - 94 Percent'
    )
    Medical_Maximum_Out_Of_Pocket___Family__Per_Person____94_Percent: str = Field(
        ..., alias='Medical Maximum Out Of Pocket - Family (Per Person) - 94 Percent'
    )
    Drug_Maximum_Out_Of_Pocket___Family__Per_Person____94_Percent: str = Field(
        ..., alias='Drug Maximum Out Of Pocket - Family (Per Person) - 94 Percent'
    )
    Primary_Care_Physician___94_Percent: str = Field(
        ..., alias='Primary Care Physician - 94 Percent'
    )
    Specialist___94_Percent: str = Field(..., alias='Specialist - 94 Percent')
    Emergency_Room___94_Percent: str = Field(..., alias='Emergency Room - 94 Percent')
    Inpatient_Facility___94_Percent: str = Field(
        ..., alias='Inpatient Facility - 94 Percent'
    )
    Inpatient_Physician___94_Percent: str = Field(
        ..., alias='Inpatient Physician - 94 Percent'
    )
    Generic_Drugs___94_Percent: str = Field(..., alias='Generic Drugs - 94 Percent')
    Preferred_Brand_Drugs___94_Percent: str = Field(
        ..., alias='Preferred Brand Drugs - 94 Percent'
    )
    Non_preferred_Brand_Drugs___94_Percent: str = Field(
        ..., alias='Non-preferred Brand Drugs - 94 Percent'
    )
    Specialty_Drugs___94_Percent: str = Field(..., alias='Specialty Drugs - 94 Percent')


class MarketplacePlanJSON(BaseModel):
    state_code: str
    fips_county_code: int
    county_name: str
    metal_level: str
    issuer_name: str
    hios_issuer_id: int
    plan_id_standard_component: str
    plan_marketing_name: str
    standardized_plan_option: str
    plan_type: str
    rating_area: str
    child_only_offering: str
    source: str
    customer_service_phone_number_local: Optional[str]
    customer_service_phone_number_toll_free: Optional[str]
    customer_service_phone_number_tty: Optional[Union[int, str]]
    network_url: str
    plan_brochure_url: Optional[str]
    summary_of_benefits_url: str
    drug_formulary_url: str
    adult_dental: Optional[str]
    child_dental: Optional[str]
    ehb_percent_of_total_premium: str
    premium_child_age_0_14: float
    premium_child_age_18: float
    premium_adult_individual_age_21: float
    premium_adult_individual_age_27: float
    premium_adult_individual_age_30: float
    premium_adult_individual_age_40: float
    premium_adult_individual_age_50: float
    premium_adult_individual_age_60: float
    premium_couple_21: float
    premium_couple_30: float
    premium_couple_40: float
    premium_couple_50: float
    premium_couple_60: float
    couple_plus_1_child_age_21: float
    couple_plus_1_child_age_30: float
    couple_plus_1_child_age_40: float
    couple_plus_1_child_age_50: float
    couple_plus_2_children_age_21: float
    couple_plus_2_children_age_30: float
    couple_plus_2_children_age_40: float
    couple_plus_2_children_age_50: float
    couple_plus_3_or_more_children_age_21: float
    couple_plus_3_or_more_children_age_30: float
    couple_plus_3_or_more_children_age_40: float
    couple_plus_3_or_more_children_age_50: float
    individual_plus_1_child_age_21: float
    individual_plus_1_child_age_30: float
    individual_plus_1_child_age_40: float
    individual_plus_1_child_age_50: float
    individual_plus_2_children_age_21: float
    individual_plus_2_children_age_30: float
    individual_plus_2_children_age_40: float
    individual_plus_2_children_age_50: float
    individual_plus_3_or_more_children_age_21: float
    individual_plus_3_or_more_children_age_30: float
    individual_plus_3_or_more_children_age_40: float
    individual_plus_3_or_more_children_age_50: float
    medical_deductible_individual_standard: float
    drug_deductible_individual_standard: Union[float, str]
    medical_deductible_family_standard: float
    drug_deductible_family_standard: Union[float, str]
    medical_deductible_family_per_person_standard: Union[float, str]
    drug_deductible_family_per_person_standard: Union[float, str]
    medical_maximum_out_of_pocket_individual_standard: float
    drug_maximum_out_of_pocket_individual_standard: Union[float, str]
    medical_maximum_out_of_pocket_family_standard: float
    drug_maximum_out_of_pocket_family_standard: Union[float, str]
    medical_maximum_out_of_pocket_family_per_person_standard: float
    drug_maximum_out_of_pocket_family_per_person_standard: Union[float, str]
    primary_care_physician_standard: Union[float, str]
    specialist_standard: Union[float, str]
    emergency_room_standard: Union[float, str]
    inpatient_facility_standard: str
    inpatient_physician_standard: Union[float, str]
    generic_drugs_standard: Union[float, str]
    preferred_brand_drugs_standard: Union[float, str]
    non_preferred_brand_drugs_standard: Union[float, str]
    specialty_drugs_standard: Union[float, str]
    col_73_percent_actuarial_value_silver_plan_cost_sharing: None
    medical_deductible_individual_73_percent: Optional[float]
    drug_deductible_individual_73_percent: Optional[Union[float, str]]
    medical_deductible_family_73_percent: Optional[float]
    drug_deductible_family_73_percent: Optional[Union[float, str]]
    medical_deductible_family_per_person_73_percent: Optional[float]
    drug_deductible_family_per_person_73_percent: Optional[Union[float, str]]
    medical_maximum_out_of_pocket_individual_73_percent: Optional[float]
    drug_maximum_out_of_pocket_individual_73_percent: Optional[str]
    medical_maximum_out_of_pocket_family_73_percent: Optional[float]
    drug_maximum_out_of_pocket_family_73_percent: Optional[str]
    medical_maximum_out_of_pocket_family_per_person_73_percent: Optional[float]
    drug_maximum_out_of_pocket_family_per_person_73_percent: Optional[str]
    primary_care_physician_73_percent: Optional[Union[float, str]]
    specialist_73_percent: Optional[Union[float, str]]
    emergency_room_73_percent: Optional[Union[float, str]]
    inpatient_facility_73_percent: Optional[str]
    inpatient_physician_73_percent: Optional[Union[float, str]]
    generic_drugs_73_percent: Optional[Union[float, str]]
    preferred_brand_drugs_73_percent: Optional[Union[float, str]]
    non_preferred_brand_drugs_73_percent: Optional[Union[float, str]]
    specialty_drugs_73_percent: Optional[Union[float, str]]
    col_87_percent_actuarial_value_silver_plan_cost_sharing: None
    medical_deductible_individual_87_percent: Optional[float]
    drug_deductible_individual_87_percent: Optional[Union[float, str]]
    medical_deductible_family_87_percent: Optional[float]
    drug_deductible_family_87_percent: Optional[Union[float, str]]
    medical_deductible_family_per_person_87_percent: Optional[float]
    drug_deductible_family_per_person_87_percent: Optional[Union[float, str]]
    medical_maximum_out_of_pocket_individual_87_percent: Optional[float]
    drug_maximum_out_of_pocket_individual_87_percent: Optional[str]
    medical_maximum_out_of_pocket_family_87_percent: Optional[float]
    drug_maximum_out_of_pocket_family_87_percent: Optional[str]
    medical_maximum_out_of_pocket_family_per_person_87_percent: Optional[float]
    drug_maximum_out_of_pocket_family_per_person_87_percent: Optional[str]
    primary_care_physician_87_percent: Optional[Union[float, str]]
    specialist_87_percent: Optional[Union[float, str]]
    emergency_room_87_percent: Optional[Union[float, str]]
    inpatient_facility_87_percent: Optional[str]
    inpatient_physician_87_percent: Optional[Union[float, str]]
    generic_drugs_87_percent: Optional[Union[float, str]]
    preferred_brand_drugs_87_percent: Optional[Union[float, str]]
    non_preferred_brand_drugs_87_percent: Optional[Union[float, str]]
    specialty_drugs_87_percent: Optional[Union[float, str]]
    col_94_percent_actuarial_value_silver_plan_cost_sharing: None
    medical_deductible_individual_94_percent: Optional[float]
    drug_deductible_individual_94_percent: Optional[Union[float, str]]
    medical_deductible_family_94_percent: Optional[float]
    drug_deductible_family_94_percent: Optional[Union[float, str]]
    medical_deductible_family_per_person_94_percent: Optional[float]
    drug_deductible_family_per_person_94_percent: Optional[Union[float, str]]
    medical_maximum_out_of_pocket_individual_94_percent: Optional[float]
    drug_maximum_out_of_pocket_individual_94_percent: Optional[str]
    medical_maximum_out_of_pocket_family_94_percent: Optional[float]
    drug_maximum_out_of_pocket_family_94_percent: Optional[str]
    medical_maximum_out_of_pocket_family_per_person_94_percent: Optional[float]
    drug_maximum_out_of_pocket_family_per_person_94_percent: Optional[str]
    primary_care_physician_94_percent: Optional[Union[float, str]]
    specialist_94_percent: Optional[Union[float, str]]
    emergency_room_94_percent: Optional[Union[float, str]]
    inpatient_facility_94_percent: Optional[str]
    inpatient_physician_94_percent: Optional[Union[float, str]]
    generic_drugs_94_percent: Optional[Union[float, str]]
    preferred_brand_drugs_94_percent: Optional[Union[float, str]]
    non_preferred_brand_drugs_94_percent: Optional[Union[float, str]]
    specialty_drugs_94_percent: Optional[Union[float, str]]



class Model(RootModel[List[MarketplacePlanJSON]]):
    root: List[MarketplacePlanJSON]
