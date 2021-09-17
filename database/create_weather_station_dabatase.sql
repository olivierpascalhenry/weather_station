
-- creation de lutilisateur
CREATE ROLE weather_station WITH LOGIN NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION ENCRYPTED PASSWORD 'SCRAM-SHA-256$4096:GbCeylkmUVEs9C07nSJ35Q==$y9Eq7SWQgSBEtiCkOhaSGY+MKGcPm+jkf90nyItCR5A=:ZS0OzbUbnFFncaAs1C7YlsQGGew+Oomw6UpnhVBNOmo=';

-- creation de la base de donnees
CREATE DATABASE weather_station_db WITH OWNER = weather_station ENCODING = 'UTF8' TABLESPACE = pg_default CONNECTION LIMIT = -1;
GRANT ALL ON DATABASE weather_station_db TO weather_station;
GRANT TEMPORARY, CONNECT ON DATABASE weather_station_db TO PUBLIC;

-- creation des sequences
CREATE SEQUENCE public.ext_temp_id_seq INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;
ALTER SEQUENCE public.ext_temp_id_seq OWNER TO weather_station;

CREATE SEQUENCE public.int_hum_id_seq INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;
ALTER SEQUENCE public.int_hum_id_seq OWNER TO weather_station;

CREATE SEQUENCE public.int_temp_id_seq INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;
ALTER SEQUENCE public.int_temp_id_seq OWNER TO weather_station;

CREATE SEQUENCE public.int_pres_id_seq INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;
ALTER SEQUENCE public.int_pres_id_seq OWNER TO weather_station;

-- creation des tables
CREATE TABLE IF NOT EXISTS public.ext_temp (id integer NOT NULL DEFAULT nextval('ext_temp_id_seq'::regclass), ext_tp_time timestamp without time zone NOT NULL, ext_tp_data real NOT NULL, CONSTRAINT ext_temp_pkey PRIMARY KEY (id)) TABLESPACE pg_default;
ALTER TABLE public.ext_temp OWNER to weather_station;

CREATE TABLE IF NOT EXISTS public.int_hum (id integer NOT NULL DEFAULT nextval('int_hum_id_seq'::regclass), int_hd_time timestamp without time zone NOT NULL, int_hd_data real NOT NULL, CONSTRAINT int_hum_pkey PRIMARY KEY (id)) TABLESPACE pg_default;
ALTER TABLE public.int_hum OWNER to weather_station;

CREATE TABLE IF NOT EXISTS public.int_temp (id integer NOT NULL DEFAULT nextval('int_temp_id_seq'::regclass), int_tp_time timestamp without time zone NOT NULL, int_tp_data real NOT NULL, CONSTRAINT int_temp_pkey PRIMARY KEY (id)) TABLESPACE pg_default;
ALTER TABLE public.int_temp OWNER to weather_station;

CREATE TABLE IF NOT EXISTS public.int_pres (id integer NOT NULL DEFAULT nextval('int_pres_id_seq'::regclass), int_ps_time timestamp without time zone NOT NULL, int_ps_data real NOT NULL, CONSTRAINT int_pres_pkey PRIMARY KEY (id)) TABLESPACE pg_default;
ALTER TABLE public.int_pres OWNER to weather_station;