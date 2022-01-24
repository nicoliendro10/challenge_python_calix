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

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO postgres;

--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: cine; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cine (
    provincia text,
    pantallas bigint,
    butacas bigint,
    espacio_incaa text,
    "timestamp" timestamp without time zone
);


ALTER TABLE public.cine OWNER TO postgres;

--
-- Name: datos_conjuntos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.datos_conjuntos (
    categoria text,
    "Total records" bigint,
    fuente text,
    idprovincia double precision,
    "timestamp" timestamp without time zone
);


ALTER TABLE public.datos_conjuntos OWNER TO postgres;

--
-- Name: institucion_cultural; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.institucion_cultural (
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
    web text,
    "timestamp" timestamp without time zone
);


ALTER TABLE public.institucion_cultural OWNER TO postgres;

--
-- PostgreSQL database dump complete
--

