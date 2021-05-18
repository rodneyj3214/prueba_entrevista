create sequence sec_weather
	start with 1
  	increment by 1
	maxvalue 99999
	minvalue 1;
-- Table: public.weather

-- DROP TABLE public.weather;
CREATE TABLE weather
(
    id bigint NOT NULL DEFAULT nextval('sec_test'::regclass),
    type_weather character varying NOT NULL,
    date_at timestamp(0) without time zone DEFAULT NOW(),
	value_number numeric,
    CONSTRAINT weather_pkey PRIMARY KEY (id)
   
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;
