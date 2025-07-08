-- Create a view showing distinct state codes and county names
-- This view provides a clean lookup table for all available state/county combinations

CREATE VIEW state_county_lookup AS
SELECT DISTINCT
    state_code,
    county_name,
    fips_county_code
FROM marketplace_plans
ORDER BY state_code, county_name;

-- Add comment for documentation
COMMENT ON VIEW state_county_lookup IS 'View showing distinct state codes and county names available in marketplace plans data';
COMMENT ON COLUMN state_county_lookup.state_code IS 'Two-letter state abbreviation';
COMMENT ON COLUMN state_county_lookup.county_name IS 'County name';
COMMENT ON COLUMN state_county_lookup.fips_county_code IS 'Federal Information Processing Standard county code';
