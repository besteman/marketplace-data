-- Create table for marketplace health insurance plans
-- Generated from MarketplacePlanJSON Pydantic model

CREATE TABLE marketplace_plans (
    -- Primary key
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,

    -- Primary identification fields
    state_code VARCHAR(2) NOT NULL,
    fips_county_code INTEGER NOT NULL,
    county_name VARCHAR(255) NOT NULL,
    metal_level VARCHAR(50) NOT NULL,
    issuer_name VARCHAR(255) NOT NULL,
    hios_issuer_id INTEGER NOT NULL,
    plan_id_standard_component VARCHAR(100) NOT NULL,
    plan_marketing_name VARCHAR(255) NOT NULL,
    standardized_plan_option VARCHAR(100) NOT NULL,
    plan_type VARCHAR(50) NOT NULL,
    rating_area VARCHAR(50) NOT NULL,
    child_only_offering VARCHAR(50) NOT NULL,
    source VARCHAR(100) NOT NULL,

    -- Contact information
    customer_service_phone_number_local VARCHAR(50),
    customer_service_phone_number_toll_free VARCHAR(50),
    customer_service_phone_number_tty VARCHAR(50),

    -- URLs
    network_url TEXT NOT NULL,
    plan_brochure_url TEXT,
    summary_of_benefits_url TEXT NOT NULL,
    drug_formulary_url TEXT NOT NULL,

    -- Dental coverage
    adult_dental VARCHAR(50),
    child_dental VARCHAR(50),

    -- Premium information
    ehb_percent_of_total_premium VARCHAR(20) NOT NULL,
    premium_child_age_0_14 DECIMAL(10,2) NOT NULL,
    premium_child_age_18 DECIMAL(10,2) NOT NULL,
    premium_adult_individual_age_21 DECIMAL(10,2) NOT NULL,
    premium_adult_individual_age_27 DECIMAL(10,2) NOT NULL,
    premium_adult_individual_age_30 DECIMAL(10,2) NOT NULL,
    premium_adult_individual_age_40 DECIMAL(10,2) NOT NULL,
    premium_adult_individual_age_50 DECIMAL(10,2) NOT NULL,
    premium_adult_individual_age_60 DECIMAL(10,2) NOT NULL,
    premium_couple_21 DECIMAL(10,2) NOT NULL,
    premium_couple_30 DECIMAL(10,2) NOT NULL,
    premium_couple_40 DECIMAL(10,2) NOT NULL,
    premium_couple_50 DECIMAL(10,2) NOT NULL,
    premium_couple_60 DECIMAL(10,2) NOT NULL,

    -- Family premium information
    couple_plus_1_child_age_21 DECIMAL(10,2) NOT NULL,
    couple_plus_1_child_age_30 DECIMAL(10,2) NOT NULL,
    couple_plus_1_child_age_40 DECIMAL(10,2) NOT NULL,
    couple_plus_1_child_age_50 DECIMAL(10,2) NOT NULL,
    couple_plus_2_children_age_21 DECIMAL(10,2) NOT NULL,
    couple_plus_2_children_age_30 DECIMAL(10,2) NOT NULL,
    couple_plus_2_children_age_40 DECIMAL(10,2) NOT NULL,
    couple_plus_2_children_age_50 DECIMAL(10,2) NOT NULL,
    couple_plus_3_or_more_children_age_21 DECIMAL(10,2) NOT NULL,
    couple_plus_3_or_more_children_age_30 DECIMAL(10,2) NOT NULL,
    couple_plus_3_or_more_children_age_40 DECIMAL(10,2) NOT NULL,
    couple_plus_3_or_more_children_age_50 DECIMAL(10,2) NOT NULL,

    -- Individual with children premium information
    individual_plus_1_child_age_21 DECIMAL(10,2) NOT NULL,
    individual_plus_1_child_age_30 DECIMAL(10,2) NOT NULL,
    individual_plus_1_child_age_40 DECIMAL(10,2) NOT NULL,
    individual_plus_1_child_age_50 DECIMAL(10,2) NOT NULL,
    individual_plus_2_children_age_21 DECIMAL(10,2) NOT NULL,
    individual_plus_2_children_age_30 DECIMAL(10,2) NOT NULL,
    individual_plus_2_children_age_40 DECIMAL(10,2) NOT NULL,
    individual_plus_2_children_age_50 DECIMAL(10,2) NOT NULL,
    individual_plus_3_or_more_children_age_21 DECIMAL(10,2) NOT NULL,
    individual_plus_3_or_more_children_age_30 DECIMAL(10,2) NOT NULL,
    individual_plus_3_or_more_children_age_40 DECIMAL(10,2) NOT NULL,
    individual_plus_3_or_more_children_age_50 DECIMAL(10,2) NOT NULL,

    -- Standard deductibles and maximums
    medical_deductible_individual_standard DECIMAL(10,2) NOT NULL,
    drug_deductible_individual_standard VARCHAR(50), -- Can be text like "See Medical Deductible"
    medical_deductible_family_standard DECIMAL(10,2) NOT NULL,
    drug_deductible_family_standard VARCHAR(50), -- Can be text like "See Medical Deductible"
    medical_deductible_family_per_person_standard VARCHAR(50), -- Can be text or numeric
    drug_deductible_family_per_person_standard VARCHAR(50), -- Can be text or numeric
    medical_maximum_out_of_pocket_individual_standard DECIMAL(10,2) NOT NULL,
    drug_maximum_out_of_pocket_individual_standard VARCHAR(50), -- Can be text like "No Charge"
    medical_maximum_out_of_pocket_family_standard DECIMAL(10,2) NOT NULL,
    drug_maximum_out_of_pocket_family_standard VARCHAR(50), -- Can be text like "No Charge"
    medical_maximum_out_of_pocket_family_per_person_standard DECIMAL(10,2) NOT NULL,
    drug_maximum_out_of_pocket_family_per_person_standard VARCHAR(50), -- Can be text like "No Charge"

    -- Standard copays/coinsurance
    primary_care_physician_standard VARCHAR(50), -- Can be dollar amount or percentage
    specialist_standard VARCHAR(50), -- Can be dollar amount or percentage
    emergency_room_standard VARCHAR(50), -- Can be dollar amount or percentage
    inpatient_facility_standard VARCHAR(100) NOT NULL, -- Usually text like "Coinsurance"
    inpatient_physician_standard VARCHAR(50), -- Can be dollar amount or percentage
    generic_drugs_standard VARCHAR(50), -- Can be dollar amount or percentage
    preferred_brand_drugs_standard VARCHAR(50), -- Can be dollar amount or percentage
    non_preferred_brand_drugs_standard VARCHAR(50), -- Can be dollar amount or percentage
    specialty_drugs_standard VARCHAR(50), -- Can be dollar amount or percentage

    -- 73% Actuarial Value Silver Plan Cost Sharing
    col_73_percent_actuarial_value_silver_plan_cost_sharing VARCHAR(50), -- Usually NULL
    medical_deductible_individual_73_percent DECIMAL(10,2),
    drug_deductible_individual_73_percent VARCHAR(50),
    medical_deductible_family_73_percent DECIMAL(10,2),
    drug_deductible_family_73_percent VARCHAR(50),
    medical_deductible_family_per_person_73_percent DECIMAL(10,2),
    drug_deductible_family_per_person_73_percent VARCHAR(50),
    medical_maximum_out_of_pocket_individual_73_percent DECIMAL(10,2),
    drug_maximum_out_of_pocket_individual_73_percent VARCHAR(50),
    medical_maximum_out_of_pocket_family_73_percent DECIMAL(10,2),
    drug_maximum_out_of_pocket_family_73_percent VARCHAR(50),
    medical_maximum_out_of_pocket_family_per_person_73_percent DECIMAL(10,2),
    drug_maximum_out_of_pocket_family_per_person_73_percent VARCHAR(50),
    primary_care_physician_73_percent VARCHAR(50),
    specialist_73_percent VARCHAR(50),
    emergency_room_73_percent VARCHAR(50),
    inpatient_facility_73_percent VARCHAR(100),
    inpatient_physician_73_percent VARCHAR(50),
    generic_drugs_73_percent VARCHAR(50),
    preferred_brand_drugs_73_percent VARCHAR(50),
    non_preferred_brand_drugs_73_percent VARCHAR(50),
    specialty_drugs_73_percent VARCHAR(50),

    -- 87% Actuarial Value Silver Plan Cost Sharing
    col_87_percent_actuarial_value_silver_plan_cost_sharing VARCHAR(50), -- Usually NULL
    medical_deductible_individual_87_percent DECIMAL(10,2),
    drug_deductible_individual_87_percent VARCHAR(50),
    medical_deductible_family_87_percent DECIMAL(10,2),
    drug_deductible_family_87_percent VARCHAR(50),
    medical_deductible_family_per_person_87_percent DECIMAL(10,2),
    drug_deductible_family_per_person_87_percent VARCHAR(50),
    medical_maximum_out_of_pocket_individual_87_percent DECIMAL(10,2),
    drug_maximum_out_of_pocket_individual_87_percent VARCHAR(50),
    medical_maximum_out_of_pocket_family_87_percent DECIMAL(10,2),
    drug_maximum_out_of_pocket_family_87_percent VARCHAR(50),
    medical_maximum_out_of_pocket_family_per_person_87_percent DECIMAL(10,2),
    drug_maximum_out_of_pocket_family_per_person_87_percent VARCHAR(50),
    primary_care_physician_87_percent VARCHAR(50),
    specialist_87_percent VARCHAR(50),
    emergency_room_87_percent VARCHAR(50),
    inpatient_facility_87_percent VARCHAR(100),
    inpatient_physician_87_percent VARCHAR(50),
    generic_drugs_87_percent VARCHAR(50),
    preferred_brand_drugs_87_percent VARCHAR(50),
    non_preferred_brand_drugs_87_percent VARCHAR(50),
    specialty_drugs_87_percent VARCHAR(50),

    -- 94% Actuarial Value Silver Plan Cost Sharing
    col_94_percent_actuarial_value_silver_plan_cost_sharing VARCHAR(50), -- Usually NULL
    medical_deductible_individual_94_percent DECIMAL(10,2),
    drug_deductible_individual_94_percent VARCHAR(50),
    medical_deductible_family_94_percent DECIMAL(10,2),
    drug_deductible_family_94_percent VARCHAR(50),
    medical_deductible_family_per_person_94_percent DECIMAL(10,2),
    drug_deductible_family_per_person_94_percent VARCHAR(50),
    medical_maximum_out_of_pocket_individual_94_percent DECIMAL(10,2),
    drug_maximum_out_of_pocket_individual_94_percent VARCHAR(50),
    medical_maximum_out_of_pocket_family_94_percent DECIMAL(10,2),
    drug_maximum_out_of_pocket_family_94_percent VARCHAR(50),
    medical_maximum_out_of_pocket_family_per_person_94_percent DECIMAL(10,2),
    drug_maximum_out_of_pocket_family_per_person_94_percent VARCHAR(50),
    primary_care_physician_94_percent VARCHAR(50),
    specialist_94_percent VARCHAR(50),
    emergency_room_94_percent VARCHAR(50),
    inpatient_facility_94_percent VARCHAR(100),
    inpatient_physician_94_percent VARCHAR(50),
    generic_drugs_94_percent VARCHAR(50),
    preferred_brand_drugs_94_percent VARCHAR(50),
    non_preferred_brand_drugs_94_percent VARCHAR(50),
    specialty_drugs_94_percent VARCHAR(50),

    -- Metadata
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for common query patterns
CREATE INDEX idx_marketplace_plans_state_county ON marketplace_plans(state_code, fips_county_code);
CREATE INDEX idx_marketplace_plans_issuer ON marketplace_plans(hios_issuer_id);
CREATE INDEX idx_marketplace_plans_metal_level ON marketplace_plans(metal_level);
CREATE INDEX idx_marketplace_plans_plan_type ON marketplace_plans(plan_type);
CREATE INDEX idx_marketplace_plans_plan_id ON marketplace_plans(plan_id_standard_component);

-- Create a unique constraint on business key fields (removing the primary key constraint)
ALTER TABLE marketplace_plans ADD CONSTRAINT uk_marketplace_plans_business_key
    UNIQUE (state_code, fips_county_code, plan_id_standard_component);

-- Add comments for documentation
COMMENT ON TABLE marketplace_plans IS 'Marketplace health insurance plans data converted from CSV using MarketplacePlanJSON Pydantic model';
COMMENT ON COLUMN marketplace_plans.id IS 'Primary key - auto-generated UUID';
COMMENT ON COLUMN marketplace_plans.state_code IS 'Two-letter state abbreviation';
COMMENT ON COLUMN marketplace_plans.fips_county_code IS 'Federal Information Processing Standard county code';
COMMENT ON COLUMN marketplace_plans.ehb_percent_of_total_premium IS 'Essential Health Benefits percentage of total premium';
COMMENT ON COLUMN marketplace_plans.col_73_percent_actuarial_value_silver_plan_cost_sharing IS 'Column for 73% actuarial value silver plan cost sharing (prefixed with col_ due to starting with number)';
COMMENT ON COLUMN marketplace_plans.col_87_percent_actuarial_value_silver_plan_cost_sharing IS 'Column for 87% actuarial value silver plan cost sharing (prefixed with col_ due to starting with number)';
COMMENT ON COLUMN marketplace_plans.col_94_percent_actuarial_value_silver_plan_cost_sharing IS 'Column for 94% actuarial value silver plan cost sharing (prefixed with col_ due to starting with number)';
