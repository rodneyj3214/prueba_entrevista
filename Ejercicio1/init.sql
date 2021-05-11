create sequence sec_test
	start with 1
  	increment by 1
	maxvalue 99999
	minvalue 1;
--select * from test
CREATE TABLE test
(
    id bigint NOT NULL DEFAULT nextval('sec_test'::regclass),
    change_value numeric NOT NULL,
    date_coin timestamp(0) without time zone,
	name_coin character varying,
    CONSTRAINT role_user_pkey PRIMARY KEY (id)
   
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;
