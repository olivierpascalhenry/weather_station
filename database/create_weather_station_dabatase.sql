
-- creation de lutilisateur
CREATE ROLE weather_station WITH LOGIN NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION ENCRYPTED PASSWORD 'SCRAM-SHA-256$4096:GbCeylkmUVEs9C07nSJ35Q==$y9Eq7SWQgSBEtiCkOhaSGY+MKGcPm+jkf90nyItCR5A=:ZS0OzbUbnFFncaAs1C7YlsQGGew+Oomw6UpnhVBNOmo=';

-- creation de la base de donnees
CREATE DATABASE weather_station_db WITH OWNER = weather_station ENCODING = 'UTF8' TABLESPACE = pg_default CONNECTION LIMIT = -1;
GRANT ALL ON DATABASE weather_station_db TO weather_station;
GRANT TEMPORARY, CONNECT ON DATABASE weather_station_db TO PUBLIC;

-- !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
-- se connecter à la base weather_station_db avant de dérouler la suite
-- !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

-- creation des tables
CREATE TABLE IF NOT EXISTS public."DS18B20" (date_time timestamp without time zone NOT NULL, temperature real, CONSTRAINT "DS18B20_pkey" PRIMARY KEY (date_time)) TABLESPACE pg_default;
ALTER TABLE public."DS18B20" OWNER to weather_station;
COMMENT ON TABLE public."DS18B20" IS 'Table dédiée au capteur DS18B20';

CREATE TABLE IF NOT EXISTS public."BME280" (date_time timestamp without time zone NOT NULL, temperature real, pression real, pression_msl real, humidite real, CONSTRAINT "BME280_pkey" PRIMARY KEY (date_time)) TABLESPACE pg_default;
ALTER TABLE public."BME280" OWNER to weather_station;
COMMENT ON TABLE public."BME280" IS 'Table dédiée au capteur BME280';

CREATE TABLE IF NOT EXISTS public."AQARA_THP" (date_time timestamp without time zone NOT NULL, temperature real, humidite real, pression real, pression_msl real, batterie real, qualite real, CONSTRAINT "AQARA_THP_pkey" PRIMARY KEY (date_time)) TABLESPACE pg_default;
ALTER TABLE public."AQARA_THP" OWNER to weather_station;
COMMENT ON TABLE public."AQARA_THP" IS 'table dédiée au capteur Aqara de température, pression, humidité';
