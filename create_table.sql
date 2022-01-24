--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1
-- Dumped by pg_dump version 14.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: institucion_cultural; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.institucion_cultural (
    index bigint,
    cod_loc bigint,
    idprovincia bigint,
    iddepartamento bigint,
    categoria text,
    provincia text,
    localidad text,
    nombre text,
    direccion text,
    cp text,
    telefono text,
    mail text,
    web text
);


ALTER TABLE public.institucion_cultural OWNER TO postgres;

--
-- Name: ix_institucion_cultural_index; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_institucion_cultural_index ON public.institucion_cultural USING btree (index);


--
-- PostgreSQL database dump complete
--

