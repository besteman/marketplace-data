-- Update database schema to fix field length issues
-- Based on upload errors encountered during data import

-- First, let's check the current data to see maximum lengths
-- (Run these queries to understand the data better if needed)

-- Increase field lengths that were causing errors
ALTER TABLE marketplace_plans
    ALTER COLUMN plan_marketing_name TYPE VARCHAR(500);

-- URLs should already be TEXT, but let's ensure they're properly sized
-- (These should already be TEXT from the original schema, but confirming)

-- Phone number fields might need more space
ALTER TABLE marketplace_plans
    ALTER COLUMN customer_service_phone_number_local TYPE VARCHAR(100),
    ALTER COLUMN customer_service_phone_number_toll_free TYPE VARCHAR(100),
    ALTER COLUMN customer_service_phone_number_tty TYPE VARCHAR(100);

-- Plan identification fields that might need more space
ALTER TABLE marketplace_plans
    ALTER COLUMN plan_id_standard_component TYPE VARCHAR(200),
    ALTER COLUMN standardized_plan_option TYPE VARCHAR(200);

-- Other fields that commonly have longer values
ALTER TABLE marketplace_plans
    ALTER COLUMN metal_level TYPE VARCHAR(100),
    ALTER COLUMN plan_type TYPE VARCHAR(100),
    ALTER COLUMN rating_area TYPE VARCHAR(100),
    ALTER COLUMN child_only_offering TYPE VARCHAR(100);

-- Dental coverage fields
ALTER TABLE marketplace_plans
    ALTER COLUMN adult_dental TYPE VARCHAR(100),
    ALTER COLUMN child_dental TYPE VARCHAR(100);

-- EHB percentage field might need more space for longer descriptions
ALTER TABLE marketplace_plans
    ALTER COLUMN ehb_percent_of_total_premium TYPE VARCHAR(100);

-- All the deductible and cost-sharing text fields that might contain longer descriptions
ALTER TABLE marketplace_plans
    ALTER COLUMN drug_deductible_individual_standard TYPE VARCHAR(200),
    ALTER COLUMN drug_deductible_family_standard TYPE VARCHAR(200),
    ALTER COLUMN medical_deductible_family_per_person_standard TYPE VARCHAR(200),
    ALTER COLUMN drug_deductible_family_per_person_standard TYPE VARCHAR(200),
    ALTER COLUMN drug_maximum_out_of_pocket_individual_standard TYPE VARCHAR(200),
    ALTER COLUMN drug_maximum_out_of_pocket_family_standard TYPE VARCHAR(200),
    ALTER COLUMN drug_maximum_out_of_pocket_family_per_person_standard TYPE VARCHAR(200);

-- Cost sharing fields that might have longer descriptions
ALTER TABLE marketplace_plans
    ALTER COLUMN primary_care_physician_standard TYPE VARCHAR(200),
    ALTER COLUMN specialist_standard TYPE VARCHAR(200),
    ALTER COLUMN emergency_room_standard TYPE VARCHAR(200),
    ALTER COLUMN inpatient_facility_standard TYPE VARCHAR(200),
    ALTER COLUMN inpatient_physician_standard TYPE VARCHAR(200),
    ALTER COLUMN generic_drugs_standard TYPE VARCHAR(200),
    ALTER COLUMN preferred_brand_drugs_standard TYPE VARCHAR(200),
    ALTER COLUMN non_preferred_brand_drugs_standard TYPE VARCHAR(200),
    ALTER COLUMN specialty_drugs_standard TYPE VARCHAR(200);

-- 73% Actuarial Value fields
ALTER TABLE marketplace_plans
    ALTER COLUMN col_73_percent_actuarial_value_silver_plan_cost_sharing TYPE VARCHAR(200),
    ALTER COLUMN drug_deductible_individual_73_percent TYPE VARCHAR(200),
    ALTER COLUMN drug_deductible_family_73_percent TYPE VARCHAR(200),
    ALTER COLUMN drug_deductible_family_per_person_73_percent TYPE VARCHAR(200),
    ALTER COLUMN drug_maximum_out_of_pocket_individual_73_percent TYPE VARCHAR(200),
    ALTER COLUMN drug_maximum_out_of_pocket_family_73_percent TYPE VARCHAR(200),
    ALTER COLUMN drug_maximum_out_of_pocket_family_per_person_73_percent TYPE VARCHAR(200),
    ALTER COLUMN primary_care_physician_73_percent TYPE VARCHAR(200),
    ALTER COLUMN specialist_73_percent TYPE VARCHAR(200),
    ALTER COLUMN emergency_room_73_percent TYPE VARCHAR(200),
    ALTER COLUMN inpatient_facility_73_percent TYPE VARCHAR(200),
    ALTER COLUMN inpatient_physician_73_percent TYPE VARCHAR(200),
    ALTER COLUMN generic_drugs_73_percent TYPE VARCHAR(200),
    ALTER COLUMN preferred_brand_drugs_73_percent TYPE VARCHAR(200),
    ALTER COLUMN non_preferred_brand_drugs_73_percent TYPE VARCHAR(200),
    ALTER COLUMN specialty_drugs_73_percent TYPE VARCHAR(200);

-- 87% Actuarial Value fields
ALTER TABLE marketplace_plans
    ALTER COLUMN col_87_percent_actuarial_value_silver_plan_cost_sharing TYPE VARCHAR(200),
    ALTER COLUMN drug_deductible_individual_87_percent TYPE VARCHAR(200),
    ALTER COLUMN drug_deductible_family_87_percent TYPE VARCHAR(200),
    ALTER COLUMN drug_deductible_family_per_person_87_percent TYPE VARCHAR(200),
    ALTER COLUMN drug_maximum_out_of_pocket_individual_87_percent TYPE VARCHAR(200),
    ALTER COLUMN drug_maximum_out_of_pocket_family_87_percent TYPE VARCHAR(200),
    ALTER COLUMN drug_maximum_out_of_pocket_family_per_person_87_percent TYPE VARCHAR(200),
    ALTER COLUMN primary_care_physician_87_percent TYPE VARCHAR(200),
    ALTER COLUMN specialist_87_percent TYPE VARCHAR(200),
    ALTER COLUMN emergency_room_87_percent TYPE VARCHAR(200),
    ALTER COLUMN inpatient_facility_87_percent TYPE VARCHAR(200),
    ALTER COLUMN inpatient_physician_87_percent TYPE VARCHAR(200),
    ALTER COLUMN generic_drugs_87_percent TYPE VARCHAR(200),
    ALTER COLUMN preferred_brand_drugs_87_percent TYPE VARCHAR(200),
    ALTER COLUMN non_preferred_brand_drugs_87_percent TYPE VARCHAR(200),
    ALTER COLUMN specialty_drugs_87_percent TYPE VARCHAR(200);

-- 94% Actuarial Value fields
ALTER TABLE marketplace_plans
    ALTER COLUMN col_94_percent_actuarial_value_silver_plan_cost_sharing TYPE VARCHAR(200),
    ALTER COLUMN drug_deductible_individual_94_percent TYPE VARCHAR(200),
    ALTER COLUMN drug_deductible_family_94_percent TYPE VARCHAR(200),
    ALTER COLUMN drug_deductible_family_per_person_94_percent TYPE VARCHAR(200),
    ALTER COLUMN drug_maximum_out_of_pocket_individual_94_percent TYPE VARCHAR(200),
    ALTER COLUMN drug_maximum_out_of_pocket_family_94_percent TYPE VARCHAR(200),
    ALTER COLUMN drug_maximum_out_of_pocket_family_per_person_94_percent TYPE VARCHAR(200),
    ALTER COLUMN primary_care_physician_94_percent TYPE VARCHAR(200),
    ALTER COLUMN specialist_94_percent TYPE VARCHAR(200),
    ALTER COLUMN emergency_room_94_percent TYPE VARCHAR(200),
    ALTER COLUMN inpatient_facility_94_percent TYPE VARCHAR(200),
    ALTER COLUMN inpatient_physician_94_percent TYPE VARCHAR(200),
    ALTER COLUMN generic_drugs_94_percent TYPE VARCHAR(200),
    ALTER COLUMN preferred_brand_drugs_94_percent TYPE VARCHAR(200),
    ALTER COLUMN non_preferred_brand_drugs_94_percent TYPE VARCHAR(200),
    ALTER COLUMN specialty_drugs_94_percent TYPE VARCHAR(200);

-- Verification queries to check the changes
-- SELECT column_name, character_maximum_length
-- FROM information_schema.columns
-- WHERE table_name = 'marketplace_plans'
-- AND character_maximum_length IS NOT NULL
-- ORDER BY column_name;
