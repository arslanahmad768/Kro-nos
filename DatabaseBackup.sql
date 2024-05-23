--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2
-- Dumped by pg_dump version 16.2

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
-- Name: citext; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS citext WITH SCHEMA public;


--
-- Name: EXTENSION citext; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION citext IS 'data type for case-insensitive character strings';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: api_attachment; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.api_attachment (
    id integer NOT NULL,
    description character varying(255) NOT NULL,
    file character varying(100) NOT NULL,
    service_ticket_id integer NOT NULL
);


ALTER TABLE public.api_attachment OWNER TO postgres;

--
-- Name: api_attachment_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.api_attachment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.api_attachment_id_seq OWNER TO postgres;

--
-- Name: api_attachment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.api_attachment_id_seq OWNED BY public.api_attachment.id;


--
-- Name: api_customer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.api_customer (
    id integer NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE public.api_customer OWNER TO postgres;

--
-- Name: api_customer_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.api_customer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.api_customer_id_seq OWNER TO postgres;

--
-- Name: api_customer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.api_customer_id_seq OWNED BY public.api_customer.id;


--
-- Name: api_customer_locations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.api_customer_locations (
    id integer NOT NULL,
    customer_id integer NOT NULL,
    location_id integer NOT NULL
);


ALTER TABLE public.api_customer_locations OWNER TO postgres;

--
-- Name: api_customer_locations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.api_customer_locations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.api_customer_locations_id_seq OWNER TO postgres;

--
-- Name: api_customer_locations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.api_customer_locations_id_seq OWNED BY public.api_customer_locations.id;


--
-- Name: api_dblockdate; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.api_dblockdate (
    id integer NOT NULL,
    lock_date date
);


ALTER TABLE public.api_dblockdate OWNER TO postgres;

--
-- Name: api_dblockdate_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.api_dblockdate_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.api_dblockdate_id_seq OWNER TO postgres;

--
-- Name: api_dblockdate_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.api_dblockdate_id_seq OWNED BY public.api_dblockdate.id;


--
-- Name: api_employeeworkblock; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.api_employeeworkblock (
    id integer NOT NULL,
    start_time timestamp with time zone,
    end_time timestamp with time zone,
    mileage numeric(10,1),
    hotel boolean,
    per_diem boolean,
    employee_id integer NOT NULL,
    service_ticket_id integer NOT NULL
);


ALTER TABLE public.api_employeeworkblock OWNER TO postgres;

--
-- Name: api_employeeworkblock_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.api_employeeworkblock_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.api_employeeworkblock_id_seq OWNER TO postgres;

--
-- Name: api_employeeworkblock_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.api_employeeworkblock_id_seq OWNED BY public.api_employeeworkblock.id;


--
-- Name: api_job; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.api_job (
    id integer NOT NULL,
    status smallint NOT NULL,
    creation_date timestamp with time zone NOT NULL,
    update_date date NOT NULL,
    description character varying(255) NOT NULL,
    customer_id integer NOT NULL,
    location_id integer NOT NULL,
    created_by_id integer NOT NULL,
    number character varying(50) NOT NULL,
    number_id integer,
    requester_id integer,
    is_archive boolean NOT NULL,
    approval_id integer,
    request_date timestamp with time zone,
    CONSTRAINT api_job_number_id_check CHECK ((number_id >= 0)),
    CONSTRAINT api_job_status_check CHECK ((status >= 0))
);


ALTER TABLE public.api_job OWNER TO postgres;

--
-- Name: api_job_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.api_job_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.api_job_id_seq OWNER TO postgres;

--
-- Name: api_job_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.api_job_id_seq OWNED BY public.api_job.id;


--
-- Name: api_job_managers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.api_job_managers (
    id integer NOT NULL,
    job_id integer NOT NULL,
    manager_id integer NOT NULL
);


ALTER TABLE public.api_job_managers OWNER TO postgres;

--
-- Name: api_job_managers_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.api_job_managers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.api_job_managers_id_seq OWNER TO postgres;

--
-- Name: api_job_managers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.api_job_managers_id_seq OWNED BY public.api_job_managers.id;


--
-- Name: api_job_mechanics; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.api_job_mechanics (
    id integer NOT NULL,
    job_id integer NOT NULL,
    mechanic_id integer NOT NULL
);


ALTER TABLE public.api_job_mechanics OWNER TO postgres;

--
-- Name: api_job_mechanics_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.api_job_mechanics_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.api_job_mechanics_id_seq OWNER TO postgres;

--
-- Name: api_job_mechanics_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.api_job_mechanics_id_seq OWNED BY public.api_job_mechanics.id;


--
-- Name: api_location; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.api_location (
    id integer NOT NULL,
    name character varying(4) NOT NULL
);


ALTER TABLE public.api_location OWNER TO postgres;

--
-- Name: api_location_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.api_location_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.api_location_id_seq OWNER TO postgres;

--
-- Name: api_location_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.api_location_id_seq OWNED BY public.api_location.id;


--
-- Name: api_serviceticket; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.api_serviceticket (
    id integer NOT NULL,
    status smallint NOT NULL,
    creation_date timestamp with time zone NOT NULL,
    update_date date NOT NULL,
    date date,
    lease_name character varying(120) NOT NULL,
    comp_model character varying(120) NOT NULL,
    engine_model character varying(120) NOT NULL,
    additional_notes character varying(2400) NOT NULL,
    customer_signature character varying(100),
    customer_printed_name character varying(120) NOT NULL,
    future_work_needed character varying(500) NOT NULL,
    what_was_found character varying(1000) NOT NULL,
    what_was_performed character varying(1000) NOT NULL,
    what_was_the_call character varying(290) NOT NULL,
    connected_job_id integer NOT NULL,
    created_by_id integer,
    who_called character varying(120) NOT NULL,
    aux_temp numeric(10,1),
    comp_serial character varying(120) NOT NULL,
    compressor_oil_pressure numeric(10,1),
    compressor_oil_temp numeric(10,1),
    county character varying(120) NOT NULL,
    customer_po_wo character varying(120) NOT NULL,
    cylinder_temperature_hi1 numeric(10,1),
    cylinder_temperature_hi2 numeric(10,1),
    cylinder_temperature_hi3 numeric(10,1),
    cylinder_temperature_hi4 numeric(10,1),
    discharge1 numeric(10,1),
    discharge2 numeric(10,1),
    discharge3 numeric(10,1),
    engine_oil_pressure numeric(10,1),
    engine_oil_temp numeric(10,1),
    engine_serial character varying(120) NOT NULL,
    exhaust_temperature_hi numeric(10,1),
    exhaust_temperature_l numeric(10,1),
    exhaust_temperature_r numeric(10,1),
    hour_meter_reading numeric(10,1),
    jacket_water_pressure numeric(10,1),
    lo_hi numeric(10,1),
    manifold_pressure_hi1 numeric(10,1),
    manifold_pressure_hi2 numeric(10,1),
    manifold_pressure_l numeric(10,1),
    manifold_pressure_r numeric(10,1),
    manifold_temperature_hi numeric(10,1),
    manifold_temperature_l numeric(10,1),
    manifold_temperature_r numeric(10,1),
    mmcfd numeric(10,1),
    rpm numeric(10,1),
    safety_setting_hi1 numeric(10,1),
    safety_setting_hi2 numeric(10,1),
    safety_setting_hi3 numeric(10,1),
    safety_setting_hi4 numeric(10,1),
    safety_setting_hi5 numeric(10,1),
    safety_setting_lo1 numeric(10,1),
    safety_setting_lo2 numeric(10,1),
    safety_setting_lo3 numeric(10,1),
    safety_setting_lo4 numeric(10,1),
    safety_setting_lo5 numeric(10,1),
    state smallint,
    suction numeric(10,1),
    td1 numeric(10,1),
    td2 numeric(10,1),
    td3 numeric(10,1),
    td4 numeric(10,1),
    ts1 numeric(10,1),
    ts2 numeric(10,1),
    ts3 numeric(10,1),
    ts4 numeric(10,1),
    unit character varying(20) NOT NULL,
    unit_hours integer,
    reject_description character varying(500) NOT NULL,
    requester_id integer,
    is_archive boolean NOT NULL,
    approval_id integer,
    approved_timestamp timestamp with time zone,
    submitted_for_approval_timestamp timestamp with time zone,
    CONSTRAINT api_serviceticket_state_check CHECK ((state >= 0)),
    CONSTRAINT api_serviceticket_status_check CHECK ((status >= 0)),
    CONSTRAINT api_serviceticket_unit_hours_check CHECK ((unit_hours >= 0))
);


ALTER TABLE public.api_serviceticket OWNER TO postgres;

--
-- Name: api_serviceticket_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.api_serviceticket_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.api_serviceticket_id_seq OWNER TO postgres;

--
-- Name: api_serviceticket_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.api_serviceticket_id_seq OWNED BY public.api_serviceticket.id;


--
-- Name: api_settings; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.api_settings (
    id integer NOT NULL,
    job_number_starting_point integer NOT NULL,
    CONSTRAINT api_settings_job_number_starting_point_check CHECK ((job_number_starting_point >= 0))
);


ALTER TABLE public.api_settings OWNER TO postgres;

--
-- Name: api_settings_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.api_settings_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.api_settings_id_seq OWNER TO postgres;

--
-- Name: api_settings_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.api_settings_id_seq OWNED BY public.api_settings.id;


--
-- Name: auditlog_logentry; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auditlog_logentry (
    id integer NOT NULL,
    object_pk character varying(255) NOT NULL,
    object_id bigint,
    object_repr text NOT NULL,
    action smallint NOT NULL,
    changes text NOT NULL,
    "timestamp" timestamp with time zone NOT NULL,
    actor_id integer,
    content_type_id integer NOT NULL,
    remote_addr inet,
    additional_data jsonb,
    CONSTRAINT auditlog_logentry_action_check CHECK ((action >= 0))
);


ALTER TABLE public.auditlog_logentry OWNER TO postgres;

--
-- Name: auditlog_logentry_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auditlog_logentry_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.auditlog_logentry_id_seq OWNER TO postgres;

--
-- Name: auditlog_logentry_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auditlog_logentry_id_seq OWNED BY public.auditlog_logentry.id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.auth_group_id_seq OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.auth_group_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.auth_permission_id_seq OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: authentication_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.authentication_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    first_name character varying(50) NOT NULL,
    last_name character varying(50) NOT NULL,
    email character varying(254) NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    is_staff boolean NOT NULL,
    is_confirmed_email boolean NOT NULL,
    status smallint NOT NULL,
    sent_email_notifications boolean NOT NULL,
    sent_push_notifications boolean NOT NULL,
    manager_id integer,
    CONSTRAINT authentication_user_status_check CHECK ((status >= 0))
);


ALTER TABLE public.authentication_user OWNER TO postgres;

--
-- Name: authentication_user_groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.authentication_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.authentication_user_groups OWNER TO postgres;

--
-- Name: authentication_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.authentication_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.authentication_user_groups_id_seq OWNER TO postgres;

--
-- Name: authentication_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.authentication_user_groups_id_seq OWNED BY public.authentication_user_groups.id;


--
-- Name: authentication_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.authentication_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.authentication_user_id_seq OWNER TO postgres;

--
-- Name: authentication_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.authentication_user_id_seq OWNED BY public.authentication_user.id;


--
-- Name: authentication_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.authentication_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.authentication_user_user_permissions OWNER TO postgres;

--
-- Name: authentication_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.authentication_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.authentication_user_user_permissions_id_seq OWNER TO postgres;

--
-- Name: authentication_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.authentication_user_user_permissions_id_seq OWNED BY public.authentication_user_user_permissions.id;


--
-- Name: blacklist_blacklistedtoken; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.blacklist_blacklistedtoken (
    id integer NOT NULL,
    token text,
    expires_at timestamp with time zone NOT NULL,
    blacklisted_at timestamp with time zone NOT NULL,
    user_id integer NOT NULL,
    token_id uuid,
    CONSTRAINT token_or_id_not_null CHECK (((token_id IS NOT NULL) OR (token IS NOT NULL)))
);


ALTER TABLE public.blacklist_blacklistedtoken OWNER TO postgres;

--
-- Name: blacklist_blacklistedtoken_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.blacklist_blacklistedtoken_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.blacklist_blacklistedtoken_id_seq OWNER TO postgres;

--
-- Name: blacklist_blacklistedtoken_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.blacklist_blacklistedtoken_id_seq OWNED BY public.blacklist_blacklistedtoken.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.django_admin_log_id_seq OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.django_content_type_id_seq OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.django_migrations_id_seq OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- Name: notifications_action; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.notifications_action (
    id integer NOT NULL,
    creation_date date NOT NULL,
    update_date date NOT NULL,
    object_type smallint NOT NULL,
    connected_object_id integer NOT NULL,
    description character varying(255) NOT NULL,
    is_viewed boolean NOT NULL,
    CONSTRAINT notifications_action_connected_object_id_check CHECK ((connected_object_id >= 0)),
    CONSTRAINT notifications_action_object_type_check CHECK ((object_type >= 0))
);


ALTER TABLE public.notifications_action OWNER TO postgres;

--
-- Name: notifications_action_connected_users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.notifications_action_connected_users (
    id integer NOT NULL,
    action_id integer NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.notifications_action_connected_users OWNER TO postgres;

--
-- Name: notifications_action_connected_users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.notifications_action_connected_users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.notifications_action_connected_users_id_seq OWNER TO postgres;

--
-- Name: notifications_action_connected_users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.notifications_action_connected_users_id_seq OWNED BY public.notifications_action_connected_users.id;


--
-- Name: notifications_action_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.notifications_action_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.notifications_action_id_seq OWNER TO postgres;

--
-- Name: notifications_action_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.notifications_action_id_seq OWNED BY public.notifications_action.id;


--
-- Name: time_tracker_indirecthours; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.time_tracker_indirecthours (
    id integer NOT NULL,
    creation_date date NOT NULL,
    update_date date NOT NULL,
    date date NOT NULL,
    hours numeric(5,2) NOT NULL,
    time_code_id integer NOT NULL,
    notes character varying(255) NOT NULL,
    status smallint NOT NULL,
    is_archive boolean NOT NULL,
    CONSTRAINT time_tracker_indirecthours_status_check CHECK ((status >= 0))
);


ALTER TABLE public.time_tracker_indirecthours OWNER TO postgres;

--
-- Name: time_tracker_indirecthours_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.time_tracker_indirecthours_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.time_tracker_indirecthours_id_seq OWNER TO postgres;

--
-- Name: time_tracker_indirecthours_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.time_tracker_indirecthours_id_seq OWNED BY public.time_tracker_indirecthours.id;


--
-- Name: time_tracker_indirecthours_mechanic; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.time_tracker_indirecthours_mechanic (
    id integer NOT NULL,
    indirecthours_id integer NOT NULL,
    mechanic_id integer NOT NULL
);


ALTER TABLE public.time_tracker_indirecthours_mechanic OWNER TO postgres;

--
-- Name: time_tracker_indirecthours_mechanic_new_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.time_tracker_indirecthours_mechanic_new_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.time_tracker_indirecthours_mechanic_new_id_seq OWNER TO postgres;

--
-- Name: time_tracker_indirecthours_mechanic_new_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.time_tracker_indirecthours_mechanic_new_id_seq OWNED BY public.time_tracker_indirecthours_mechanic.id;


--
-- Name: time_tracker_timecode; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.time_tracker_timecode (
    id integer NOT NULL,
    name character varying(48) NOT NULL
);


ALTER TABLE public.time_tracker_timecode OWNER TO postgres;

--
-- Name: time_tracker_timecode_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.time_tracker_timecode_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.time_tracker_timecode_id_seq OWNER TO postgres;

--
-- Name: time_tracker_timecode_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.time_tracker_timecode_id_seq OWNED BY public.time_tracker_timecode.id;


--
-- Name: api_attachment id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_attachment ALTER COLUMN id SET DEFAULT nextval('public.api_attachment_id_seq'::regclass);


--
-- Name: api_customer id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_customer ALTER COLUMN id SET DEFAULT nextval('public.api_customer_id_seq'::regclass);


--
-- Name: api_customer_locations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_customer_locations ALTER COLUMN id SET DEFAULT nextval('public.api_customer_locations_id_seq'::regclass);


--
-- Name: api_dblockdate id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_dblockdate ALTER COLUMN id SET DEFAULT nextval('public.api_dblockdate_id_seq'::regclass);


--
-- Name: api_employeeworkblock id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_employeeworkblock ALTER COLUMN id SET DEFAULT nextval('public.api_employeeworkblock_id_seq'::regclass);


--
-- Name: api_job id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_job ALTER COLUMN id SET DEFAULT nextval('public.api_job_id_seq'::regclass);


--
-- Name: api_job_managers id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_job_managers ALTER COLUMN id SET DEFAULT nextval('public.api_job_managers_id_seq'::regclass);


--
-- Name: api_job_mechanics id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_job_mechanics ALTER COLUMN id SET DEFAULT nextval('public.api_job_mechanics_id_seq'::regclass);


--
-- Name: api_location id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_location ALTER COLUMN id SET DEFAULT nextval('public.api_location_id_seq'::regclass);


--
-- Name: api_serviceticket id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_serviceticket ALTER COLUMN id SET DEFAULT nextval('public.api_serviceticket_id_seq'::regclass);


--
-- Name: api_settings id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_settings ALTER COLUMN id SET DEFAULT nextval('public.api_settings_id_seq'::regclass);


--
-- Name: auditlog_logentry id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auditlog_logentry ALTER COLUMN id SET DEFAULT nextval('public.auditlog_logentry_id_seq'::regclass);


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: authentication_user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authentication_user ALTER COLUMN id SET DEFAULT nextval('public.authentication_user_id_seq'::regclass);


--
-- Name: authentication_user_groups id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authentication_user_groups ALTER COLUMN id SET DEFAULT nextval('public.authentication_user_groups_id_seq'::regclass);


--
-- Name: authentication_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authentication_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.authentication_user_user_permissions_id_seq'::regclass);


--
-- Name: blacklist_blacklistedtoken id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.blacklist_blacklistedtoken ALTER COLUMN id SET DEFAULT nextval('public.blacklist_blacklistedtoken_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: notifications_action id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notifications_action ALTER COLUMN id SET DEFAULT nextval('public.notifications_action_id_seq'::regclass);


--
-- Name: notifications_action_connected_users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notifications_action_connected_users ALTER COLUMN id SET DEFAULT nextval('public.notifications_action_connected_users_id_seq'::regclass);


--
-- Name: time_tracker_indirecthours id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.time_tracker_indirecthours ALTER COLUMN id SET DEFAULT nextval('public.time_tracker_indirecthours_id_seq'::regclass);


--
-- Name: time_tracker_indirecthours_mechanic id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.time_tracker_indirecthours_mechanic ALTER COLUMN id SET DEFAULT nextval('public.time_tracker_indirecthours_mechanic_new_id_seq'::regclass);


--
-- Name: time_tracker_timecode id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.time_tracker_timecode ALTER COLUMN id SET DEFAULT nextval('public.time_tracker_timecode_id_seq'::regclass);


--
-- Data for Name: api_attachment; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.api_attachment (id, description, file, service_ticket_id) FROM stdin;
\.


--
-- Data for Name: api_customer; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.api_customer (id, name) FROM stdin;
1	Tiksom
\.


--
-- Data for Name: api_customer_locations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.api_customer_locations (id, customer_id, location_id) FROM stdin;
1	1	1
\.


--
-- Data for Name: api_dblockdate; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.api_dblockdate (id, lock_date) FROM stdin;
1	\N
\.


--
-- Data for Name: api_employeeworkblock; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.api_employeeworkblock (id, start_time, end_time, mileage, hotel, per_diem, employee_id, service_ticket_id) FROM stdin;
1	2024-05-15 17:38:00+05	2024-05-17 17:37:00+05	12.0	t	t	3	1
3	2024-05-12 17:47:00+05	2024-05-14 17:47:00+05	100000.0	t	t	3	3
4	2024-05-20 17:48:00+05	2024-05-22 17:48:00+05	1000.0	t	t	3	3
2	2024-05-17 17:45:00+05	2024-05-18 17:45:00+05	\N	f	f	3	2
5	2024-05-23 18:15:00+05	2024-05-26 18:15:00+05	10000.0	t	t	3	4
6	2024-05-27 18:30:00+05	2024-05-28 19:30:00+05	10000.0	t	t	3	5
7	2024-06-02 19:37:00+05	2024-06-05 07:38:00+05	0.5	t	t	3	6
8	2024-06-09 19:40:00+05	2024-06-10 16:40:00+05	0.5	t	t	3	7
9	2024-06-12 19:43:00+05	2024-06-13 19:43:00+05	0.2	t	t	3	8
10	2024-04-28 19:42:00+05	2024-04-29 19:39:00+05	100000.0	t	t	3	9
\.


--
-- Data for Name: api_job; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.api_job (id, status, creation_date, update_date, description, customer_id, location_id, created_by_id, number, number_id, requester_id, is_archive, approval_id, request_date) FROM stdin;
1	1	2024-05-14 12:57:50.154307+05	2024-05-14	Car reparing Service	1	1	1	1	\N	\N	f	\N	\N
2	1	2024-05-14 12:59:37.721745+05	2024-05-14	Tyre repairing Service	1	1	1	a12	\N	\N	f	\N	\N
3	1	2024-05-14 13:00:03.912875+05	2024-05-14	Body color repairing	1	1	1	3	\N	\N	f	\N	\N
4	1	2024-05-14 13:00:52.891978+05	2024-05-14	CAR TYRE CHANGE	1	1	2	5	\N	\N	f	\N	\N
5	1	2024-05-14 13:55:13.233542+05	2024-05-14	edsfdf	1	1	2	2404-34366-PA4-4-UNIT 2295 SHOP MAKE READY	\N	\N	f	\N	\N
6	1	2024-05-14 13:56:04.664846+05	2024-05-14	Vehicle	1	1	2	2405-34810-OK7-WALMART 121 PLANNED PPO	\N	\N	f	\N	\N
7	1	2024-05-14 13:56:46.61294+05	2024-05-14	AC cleaning	1	1	2	2404-34131-LA7-GENERATOR TESTING	\N	\N	f	\N	\N
\.


--
-- Data for Name: api_job_managers; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.api_job_managers (id, job_id, manager_id) FROM stdin;
1	1	2
2	2	2
3	3	2
4	4	2
5	5	2
6	6	2
7	7	2
\.


--
-- Data for Name: api_job_mechanics; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.api_job_mechanics (id, job_id, mechanic_id) FROM stdin;
1	1	3
2	2	3
3	3	3
4	4	3
5	5	3
6	6	3
7	7	3
\.


--
-- Data for Name: api_location; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.api_location (id, name) FROM stdin;
1	L123
\.


--
-- Data for Name: api_serviceticket; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.api_serviceticket (id, status, creation_date, update_date, date, lease_name, comp_model, engine_model, additional_notes, customer_signature, customer_printed_name, future_work_needed, what_was_found, what_was_performed, what_was_the_call, connected_job_id, created_by_id, who_called, aux_temp, comp_serial, compressor_oil_pressure, compressor_oil_temp, county, customer_po_wo, cylinder_temperature_hi1, cylinder_temperature_hi2, cylinder_temperature_hi3, cylinder_temperature_hi4, discharge1, discharge2, discharge3, engine_oil_pressure, engine_oil_temp, engine_serial, exhaust_temperature_hi, exhaust_temperature_l, exhaust_temperature_r, hour_meter_reading, jacket_water_pressure, lo_hi, manifold_pressure_hi1, manifold_pressure_hi2, manifold_pressure_l, manifold_pressure_r, manifold_temperature_hi, manifold_temperature_l, manifold_temperature_r, mmcfd, rpm, safety_setting_hi1, safety_setting_hi2, safety_setting_hi3, safety_setting_hi4, safety_setting_hi5, safety_setting_lo1, safety_setting_lo2, safety_setting_lo3, safety_setting_lo4, safety_setting_lo5, state, suction, td1, td2, td3, td4, ts1, ts2, ts3, ts4, unit, unit_hours, reject_description, requester_id, is_archive, approval_id, approved_timestamp, submitted_for_approval_timestamp) FROM stdin;
1	4	2024-05-14 18:56:03.539271+05	2024-05-15	2024-05-15	ABC	12aacs11	2020								1	3	ABC123	\N	21221sfcer3r	\N	\N	USA	1200	\N	\N	\N	\N	\N	\N	\N	\N	\N	123343555434	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	8	\N	\N	\N	\N	\N	\N	\N	\N	\N	123	40		3	f	2	2024-05-15 12:42:33.175148+05	2024-05-15 12:39:00.401958+05
3	2	2024-05-15 12:48:52.54099+05	2024-05-15	2024-05-15	Arslan’s Lease	Audi	123434556								4	3	Arslan Called this	\N	1234adfe323	\N	\N	Pakistan		\N	\N	\N	\N	\N	\N	\N	\N	\N	Adfsfs232325453	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1000.0	109.9	\N	\N	\N	\N	100.0	\N	\N	\N	\N	3	\N	\N	\N	\N	\N	\N	\N	\N	\N	1245	100		3	f	\N	\N	2024-05-15 12:49:13.052532+05
2	2	2024-05-15 12:43:39.11776+05	2024-05-15	2024-05-15	Rwrw	3324324ffs	122443244								2	3	Waile’s Calll	\N	Sfsdfr43334	\N	\N	Rarer		\N	\N	\N	\N	\N	\N	\N	\N	\N	Sfsfsfs334434	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	3	\N	\N	\N	\N	\N	\N	\N	\N	\N	Drags	1000000		3	f	\N	\N	2024-05-15 12:50:09.459393+05
4	2	2024-05-15 13:12:04.373688+05	2024-05-15	2024-05-15	Test Lease	Sfsf3434	2022								5	3	Test Called	\N	5343dfdfe	\N	\N	Pakistan	1323sfsf	\N	\N	\N	\N	\N	\N	\N	\N	\N	1223sfs4124	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	6	\N	\N	\N	\N	\N	\N	\N	\N	\N	1213113	120		3	f	\N	\N	2024-05-15 13:12:10.545333+05
5	2	2024-05-15 13:30:30.841935+05	2024-05-15	2024-05-16	Test lease from mobile	vdhdhd24747	Hdhfjdj1234								5	3	Testing called	\N	bdhdhd27474	\N	\N	Pakistan	vdhduhdje	\N	\N	\N	\N	\N	\N	\N	\N	\N	gdhdhd123	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	5	\N	\N	\N	\N	\N	\N	\N	\N	\N	cshsud1235	72		3	f	\N	\N	2024-05-15 14:36:58.507111+05
6	2	2024-05-15 14:38:46.337828+05	2024-05-15	2024-05-15	QA	g class	31								7	3	Me	\N	4654	\N	\N			\N	\N	\N	\N	\N	\N	\N	\N	\N	4543	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	5	\N	\N	\N	\N	\N	\N	\N	\N	\N	46	2		3	f	\N	\N	2024-05-15 14:41:33.777176+05
7	2	2024-05-15 14:40:44.717724+05	2024-05-15	2024-05-15	Testing	nvg	gv								6	3	Me2	\N	5754	\N	\N			\N	\N	\N	\N	\N	\N	\N	\N	\N	eyy	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	8	\N	\N	\N	\N	\N	\N	\N	\N	\N	56	2		3	f	\N	\N	2024-05-15 14:41:45.239132+05
8	2	2024-05-15 14:43:24.90833+05	2024-05-15	2024-05-15	Majid lease	23	thg								5	3	Tik	\N	rttf	\N	\N	pk		\N	\N	\N	\N	\N	\N	\N	\N	\N	455	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	4	\N	\N	\N	\N	\N	\N	\N	\N	\N	5	5		3	f	\N	\N	2024-05-15 14:43:33.776386+05
9	2	2024-05-16 14:42:15.370976+05	2024-05-16	2024-05-16	Offline Testing	3e343432dds	121212ada21								7	3	Offline	\N	Dsfdfe34343	\N	\N	Pakistan	Abcd1234	\N	\N	\N	\N	\N	\N	\N	\N	\N	Asdas2312312321	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	4	\N	\N	\N	\N	\N	\N	\N	\N	\N	13123affasf	80		3	f	\N	\N	2024-05-16 14:47:35.109619+05
\.


--
-- Data for Name: api_settings; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.api_settings (id, job_number_starting_point) FROM stdin;
1	1
\.


--
-- Data for Name: auditlog_logentry; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auditlog_logentry (id, object_pk, object_id, object_repr, action, changes, "timestamp", actor_id, content_type_id, remote_addr, additional_data) FROM stdin;
1	1	1	Hours of 	0	{"hours": ["None", "2.00"], "update_date": ["None", "2024-05-14"], "creation_date": ["None", "2024-05-14"], "notes": ["None", "Testing"], "date": ["None", "2024-05-14"], "time_code": ["None", "1244"], "status": ["None", "1"], "is_archive": ["None", "False"], "id": ["None", "1"]}	2024-05-14 15:03:05.539987+05	3	19	127.0.0.1	\N
2	1	1	Hours of Majid Mechanic	1	{"mechanic": {"type": "m2m", "operation": "add", "objects": ["Majid Mechanic"]}}	2024-05-14 15:03:05.571485+05	3	19	127.0.0.1	\N
3	1	1		0	{"status": ["None", "1"], "customer_po_wo": ["None", ""], "engine_model": ["None", ""], "who_called": ["None", ""], "creation_date": ["None", "2024-05-14 13:56:03.539271"], "engine_serial": ["None", ""], "what_was_found": ["None", ""], "comp_model": ["None", ""], "is_archive": ["None", "False"], "update_date": ["None", "2024-05-14"], "date": ["None", "2024-05-06"], "unit": ["None", ""], "attachments": ["None", "api.Attachment.None"], "what_was_the_call": ["None", ""], "customer_printed_name": ["None", ""], "comp_serial": ["None", ""], "customer_signature": ["None", ""], "lease_name": ["None", ""], "employee_works": ["None", "api.EmployeeWorkBlock.None"], "id": ["None", "1"], "reject_description": ["None", ""], "created_by": ["None", "Majid Mechanic"], "what_was_performed": ["None", ""], "connected_job": ["None", "Job #1"], "county": ["None", ""], "additional_notes": ["None", ""], "future_work_needed": ["None", ""]}	2024-05-14 18:56:03.567918+05	3	3	127.0.0.1	\N
4	1	1	ABC	1	{"date": ["2024-05-06", "2024-05-15"], "lease_name": ["", "ABC"], "who_called": ["", "ABC123"], "county": ["", "USA"], "state": ["None", "8"], "unit": ["", "123"], "comp_serial": ["", "21221sfcer3r"], "engine_model": ["", "2020"], "engine_serial": ["", "123343555434"], "customer_po_wo": ["", "1200"], "unit_hours": ["None", "40"], "comp_model": ["", "12aacs11"]}	2024-05-15 12:38:48.518671+05	3	3	119.155.27.55	\N
5	1	1	ABC	1	{"status": ["1", "2"], "submitted_for_approval_timestamp": ["None", "2024-05-15 07:39:00.401958"], "requester": ["None", "Majid Mechanic"]}	2024-05-15 12:39:00.419944+05	3	3	119.155.27.55	\N
6	1	1	ABC	1	{"status": ["2", "4"], "approval": ["None", "Arslan Manager"], "approved_timestamp": ["None", "2024-05-15 07:42:33.175148"]}	2024-05-15 12:42:33.191519+05	2	3	127.0.0.1	\N
7	2	2	Rwrw	0	{"date": ["None", "2024-05-15"], "lease_name": ["None", "Rwrw"], "update_date": ["None", "2024-05-15"], "additional_notes": ["None", ""], "what_was_found": ["None", ""], "who_called": ["None", ""], "what_was_performed": ["None", ""], "county": ["None", "Rarer"], "connected_job": ["None", "Job #a12"], "customer_printed_name": ["None", ""], "attachments": ["None", "api.Attachment.None"], "id": ["None", "2"], "status": ["None", "1"], "state": ["None", "3"], "is_archive": ["None", "False"], "what_was_the_call": ["None", ""], "unit": ["None", "Drags"], "creation_date": ["None", "2024-05-15 07:43:39.117760"], "comp_serial": ["None", ""], "reject_description": ["None", ""], "future_work_needed": ["None", ""], "engine_model": ["None", ""], "customer_signature": ["None", ""], "created_by": ["None", "Majid Mechanic"], "employee_works": ["None", "api.EmployeeWorkBlock.None"], "engine_serial": ["None", ""], "customer_po_wo": ["None", ""], "comp_model": ["None", ""]}	2024-05-15 12:43:39.138836+05	3	3	119.155.27.55	\N
8	3	3	Arslan’s Lease	0	{"date": ["None", "2024-05-15"], "lease_name": ["None", "Arslan\\u2019s\\u00a0Lease"], "update_date": ["None", "2024-05-15"], "additional_notes": ["None", ""], "what_was_found": ["None", ""], "who_called": ["None", "Arslan\\u00a0Called\\u00a0this"], "rpm": ["None", "1000.0"], "what_was_performed": ["None", ""], "county": ["None", "Pakistan"], "connected_job": ["None", "Job #5"], "customer_printed_name": ["None", ""], "attachments": ["None", "api.Attachment.None"], "id": ["None", "3"], "status": ["None", "1"], "safety_setting_hi1": ["None", "109.9"], "state": ["None", "3"], "is_archive": ["None", "False"], "what_was_the_call": ["None", ""], "unit": ["None", "1245"], "creation_date": ["None", "2024-05-15 07:48:52.540990"], "comp_serial": ["None", "1234adfe323"], "reject_description": ["None", ""], "future_work_needed": ["None", ""], "safety_setting_lo1": ["None", "100.0"], "engine_model": ["None", "123434556"], "customer_signature": ["None", ""], "created_by": ["None", "Majid Mechanic"], "employee_works": ["None", "api.EmployeeWorkBlock.None"], "engine_serial": ["None", "Adfsfs232325453"], "customer_po_wo": ["None", ""], "unit_hours": ["None", "100"], "comp_model": ["None", "Audi"]}	2024-05-15 12:48:52.561655+05	3	3	119.155.27.55	\N
9	3	3	Arslan’s Lease	1	{"status": ["1", "2"], "submitted_for_approval_timestamp": ["None", "2024-05-15 07:49:13.052532"], "requester": ["None", "Majid Mechanic"]}	2024-05-15 12:49:13.063072+05	3	3	119.155.27.55	\N
10	2	2	Rwrw	1	{"who_called": ["", "Waile\\u2019s\\u00a0Calll"], "comp_serial": ["", "Sfsdfr43334"], "engine_model": ["", "122443244"], "engine_serial": ["", "Sfsfsfs334434"], "unit_hours": ["None", "1000000"], "comp_model": ["", "3324324ffs"]}	2024-05-15 12:50:05.060091+05	3	3	119.155.27.55	\N
11	2	2	Rwrw	1	{"status": ["1", "2"], "submitted_for_approval_timestamp": ["None", "2024-05-15 07:50:09.459393"], "requester": ["None", "Majid Mechanic"]}	2024-05-15 12:50:09.47546+05	3	3	119.155.27.55	\N
12	4	4	Test Lease	0	{"date": ["None", "2024-05-15"], "lease_name": ["None", "Test\\u00a0Lease"], "update_date": ["None", "2024-05-15"], "additional_notes": ["None", ""], "what_was_found": ["None", ""], "who_called": ["None", "Test\\u00a0Called"], "what_was_performed": ["None", ""], "county": ["None", "Pakistan"], "connected_job": ["None", "Job #2404-34366-PA4-4-UNIT 2295 SHOP MAKE READY"], "customer_printed_name": ["None", ""], "attachments": ["None", "api.Attachment.None"], "id": ["None", "4"], "status": ["None", "1"], "state": ["None", "6"], "is_archive": ["None", "False"], "what_was_the_call": ["None", ""], "unit": ["None", "1213113"], "creation_date": ["None", "2024-05-15 08:12:04.373688"], "comp_serial": ["None", "5343dfdfe"], "reject_description": ["None", ""], "future_work_needed": ["None", ""], "engine_model": ["None", "2022"], "customer_signature": ["None", ""], "created_by": ["None", "Majid Mechanic"], "employee_works": ["None", "api.EmployeeWorkBlock.None"], "engine_serial": ["None", "1223sfs4124"], "customer_po_wo": ["None", "1323sfsf"], "unit_hours": ["None", "120"], "comp_model": ["None", "Sfsf3434"]}	2024-05-15 13:12:04.392224+05	3	3	119.155.27.55	\N
13	4	4	Test Lease	1	{"status": ["1", "2"], "submitted_for_approval_timestamp": ["None", "2024-05-15 08:12:10.545333"], "requester": ["None", "Majid Mechanic"]}	2024-05-15 13:12:10.55733+05	3	3	119.155.27.55	\N
14	5	5	Test lease from mobile	0	{"date": ["None", "2024-05-16"], "lease_name": ["None", "Test\\u00a0lease\\u00a0from\\u00a0mobile"], "update_date": ["None", "2024-05-15"], "additional_notes": ["None", ""], "what_was_found": ["None", ""], "who_called": ["None", "Testing\\u00a0called"], "what_was_performed": ["None", ""], "county": ["None", "Pakistan"], "connected_job": ["None", "Job #2404-34366-PA4-4-UNIT 2295 SHOP MAKE READY"], "customer_printed_name": ["None", ""], "attachments": ["None", "api.Attachment.None"], "id": ["None", "5"], "status": ["None", "1"], "state": ["None", "5"], "is_archive": ["None", "False"], "what_was_the_call": ["None", ""], "unit": ["None", "cshsud1235"], "creation_date": ["None", "2024-05-15 08:30:30.841935"], "comp_serial": ["None", "bdhdhd27474"], "reject_description": ["None", ""], "future_work_needed": ["None", ""], "engine_model": ["None", "Hdhfjdj1234"], "customer_signature": ["None", ""], "created_by": ["None", "Majid Mechanic"], "employee_works": ["None", "api.EmployeeWorkBlock.None"], "engine_serial": ["None", "gdhdhd123"], "customer_po_wo": ["None", "vdhduhdje"], "unit_hours": ["None", "72"], "comp_model": ["None", "vdhdhd24747"]}	2024-05-15 13:30:30.86225+05	3	3	119.155.27.55	\N
15	5	5	Test lease from mobile	1	{"status": ["1", "2"], "submitted_for_approval_timestamp": ["None", "2024-05-15 09:36:58.507111"], "requester": ["None", "Majid Mechanic"]}	2024-05-15 14:36:58.51911+05	3	3	119.155.27.55	\N
16	6	6	QA	0	{"date": ["None", "2024-05-15"], "lease_name": ["None", "QA"], "update_date": ["None", "2024-05-15"], "additional_notes": ["None", ""], "what_was_found": ["None", ""], "who_called": ["None", "Me"], "what_was_performed": ["None", ""], "county": ["None", ""], "connected_job": ["None", "Job #2404-34131-LA7-GENERATOR TESTING"], "customer_printed_name": ["None", ""], "attachments": ["None", "api.Attachment.None"], "id": ["None", "6"], "status": ["None", "1"], "is_archive": ["None", "False"], "what_was_the_call": ["None", ""], "unit": ["None", "46"], "creation_date": ["None", "2024-05-15 09:38:46.337828"], "comp_serial": ["None", "4654"], "reject_description": ["None", ""], "future_work_needed": ["None", ""], "engine_model": ["None", "31"], "customer_signature": ["None", ""], "created_by": ["None", "Majid Mechanic"], "employee_works": ["None", "api.EmployeeWorkBlock.None"], "engine_serial": ["None", "4543"], "customer_po_wo": ["None", ""], "unit_hours": ["None", "2"], "comp_model": ["None", "g\\u00a0class"]}	2024-05-15 14:38:46.354877+05	3	3	119.155.27.55	\N
17	7	7	Testing	0	{"date": ["None", "2024-05-15"], "lease_name": ["None", "Testing"], "update_date": ["None", "2024-05-15"], "additional_notes": ["None", ""], "what_was_found": ["None", ""], "who_called": ["None", "Me2"], "what_was_performed": ["None", ""], "county": ["None", ""], "connected_job": ["None", "Job #2405-34810-OK7-WALMART 121 PLANNED PPO"], "customer_printed_name": ["None", ""], "attachments": ["None", "api.Attachment.None"], "id": ["None", "7"], "status": ["None", "1"], "is_archive": ["None", "False"], "what_was_the_call": ["None", ""], "unit": ["None", "56"], "creation_date": ["None", "2024-05-15 09:40:44.717724"], "comp_serial": ["None", "5754"], "reject_description": ["None", ""], "future_work_needed": ["None", ""], "engine_model": ["None", "gv"], "customer_signature": ["None", ""], "created_by": ["None", "Majid Mechanic"], "employee_works": ["None", "api.EmployeeWorkBlock.None"], "engine_serial": ["None", "eyy"], "customer_po_wo": ["None", ""], "unit_hours": ["None", "2"], "comp_model": ["None", "nvg"]}	2024-05-15 14:40:44.731605+05	3	3	119.155.27.55	\N
18	6	6	QA	1	{"state": ["None", "5"]}	2024-05-15 14:41:21.145328+05	3	3	119.155.27.55	\N
19	7	7	Testing	1	{"state": ["None", "8"]}	2024-05-15 14:41:31.061707+05	3	3	119.155.27.55	\N
20	6	6	QA	1	{"status": ["1", "2"], "submitted_for_approval_timestamp": ["None", "2024-05-15 09:41:33.777176"], "requester": ["None", "Majid Mechanic"]}	2024-05-15 14:41:33.783176+05	3	3	119.155.27.55	\N
21	7	7	Testing	1	{"status": ["1", "2"], "submitted_for_approval_timestamp": ["None", "2024-05-15 09:41:45.239132"], "requester": ["None", "Majid Mechanic"]}	2024-05-15 14:41:45.252431+05	3	3	119.155.27.55	\N
22	8	8	Majid lease	0	{"date": ["None", "2024-05-15"], "lease_name": ["None", "Majid\\u00a0lease"], "update_date": ["None", "2024-05-15"], "additional_notes": ["None", ""], "what_was_found": ["None", ""], "who_called": ["None", "Tik"], "what_was_performed": ["None", ""], "county": ["None", "pk"], "connected_job": ["None", "Job #2404-34366-PA4-4-UNIT 2295 SHOP MAKE READY"], "customer_printed_name": ["None", ""], "attachments": ["None", "api.Attachment.None"], "id": ["None", "8"], "status": ["None", "1"], "state": ["None", "4"], "is_archive": ["None", "False"], "what_was_the_call": ["None", ""], "unit": ["None", "5"], "creation_date": ["None", "2024-05-15 09:43:24.908330"], "comp_serial": ["None", "rttf"], "reject_description": ["None", ""], "future_work_needed": ["None", ""], "engine_model": ["None", "thg"], "customer_signature": ["None", ""], "created_by": ["None", "Majid Mechanic"], "employee_works": ["None", "api.EmployeeWorkBlock.None"], "engine_serial": ["None", "455"], "customer_po_wo": ["None", ""], "unit_hours": ["None", "5"], "comp_model": ["None", "23"]}	2024-05-15 14:43:24.921469+05	3	3	119.155.27.55	\N
23	8	8	Majid lease	1	{"status": ["1", "2"], "submitted_for_approval_timestamp": ["None", "2024-05-15 09:43:33.776386"], "requester": ["None", "Majid Mechanic"]}	2024-05-15 14:43:33.785728+05	3	3	119.155.27.55	\N
24	2	2	Hours of 	0	{"status": ["None", "1"], "id": ["None", "2"], "update_date": ["None", "2024-05-15"], "date": ["None", "2024-05-15"], "is_archive": ["None", "False"], "time_code": ["None", "1244"], "hours": ["None", "12.00"], "creation_date": ["None", "2024-05-15"], "notes": ["None", "good"]}	2024-05-15 14:58:32.556371+05	1	19	127.0.0.1	\N
25	2	2	Hours of Majid Mechanic	1	{"mechanic": {"type": "m2m", "operation": "add", "objects": ["Majid Mechanic"]}}	2024-05-15 14:58:32.589894+05	1	19	127.0.0.1	\N
26	3	3	Hours of 	0	{"is_archive": ["None", "False"], "notes": ["None", "Testing from mobile"], "date": ["None", "2024-05-16"], "creation_date": ["None", "2024-05-16"], "time_code": ["None", "1244"], "status": ["None", "1"], "update_date": ["None", "2024-05-16"], "hours": ["None", "24.00"], "id": ["None", "3"]}	2024-05-16 14:28:09.30386+05	3	19	119.155.2.112	\N
27	3	3	Hours of Majid Mechanic	1	{"mechanic": {"type": "m2m", "operation": "add", "objects": ["Majid Mechanic"]}}	2024-05-16 14:28:09.322857+05	3	19	119.155.2.112	\N
28	4	4	Hours of 	0	{"creation_date": ["None", "2024-05-16"], "hours": ["None", "24.00"], "is_archive": ["None", "False"], "time_code": ["None", "1244"], "date": ["None", "2024-05-16"], "update_date": ["None", "2024-05-16"], "status": ["None", "1"], "id": ["None", "4"], "notes": ["None", "Offline Testing"]}	2024-05-16 14:33:34.061734+05	3	19	119.155.2.112	\N
29	4	4	Hours of Majid Mechanic	1	{"mechanic": {"type": "m2m", "operation": "add", "objects": ["Majid Mechanic"]}}	2024-05-16 14:33:34.093144+05	3	19	119.155.2.112	\N
30	9	9	Offline Testing	0	{"engine_model": ["None", "121212ada21"], "employee_works": ["None", "api.EmployeeWorkBlock.None"], "status": ["None", "1"], "engine_serial": ["None", "Asdas2312312321"], "is_archive": ["None", "False"], "state": ["None", "4"], "id": ["None", "9"], "additional_notes": ["None", ""], "unit": ["None", "13123affasf"], "creation_date": ["None", "2024-05-16 09:42:15.370976"], "update_date": ["None", "2024-05-16"], "county": ["None", "Pakistan"], "lease_name": ["None", "Offline\\u00a0Testing"], "comp_serial": ["None", "Dsfdfe34343"], "what_was_found": ["None", ""], "customer_signature": ["None", ""], "created_by": ["None", "Majid Mechanic"], "future_work_needed": ["None", ""], "comp_model": ["None", "3e343432dds"], "customer_printed_name": ["None", ""], "connected_job": ["None", "Job #2404-34131-LA7-GENERATOR TESTING"], "reject_description": ["None", ""], "attachments": ["None", "api.Attachment.None"], "unit_hours": ["None", "80"], "what_was_performed": ["None", ""], "date": ["None", "2024-05-16"], "who_called": ["None", "Offline"], "customer_po_wo": ["None", "Abcd1234"], "what_was_the_call": ["None", ""]}	2024-05-16 14:42:15.389158+05	3	3	119.155.2.112	\N
31	9	9	Offline Testing	1	{"status": ["1", "2"], "submitted_for_approval_timestamp": ["None", "2024-05-16 09:47:35.109619"], "requester": ["None", "Majid Mechanic"]}	2024-05-16 14:47:35.123619+05	3	3	119.155.2.112	\N
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group (id, name) FROM stdin;
1	Admin
2	Biller
3	Manager
4	Mechanic
5	Superuser
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
1	2	23
2	2	27
3	2	5
4	2	8
5	2	6
6	2	7
7	2	9
8	2	15
9	2	13
10	2	19
11	2	18
12	2	83
13	3	23
14	3	27
15	3	5
16	3	8
17	3	6
18	3	7
19	3	9
20	3	12
21	3	15
22	3	13
23	3	19
24	3	18
25	3	83
26	3	85
27	3	84
28	4	8
29	4	12
30	4	15
31	4	16
32	4	13
33	4	17
34	4	80
35	4	81
36	1	1
37	1	2
38	1	3
39	1	4
40	1	5
41	1	6
42	1	7
43	1	8
44	1	9
45	1	10
46	1	11
47	1	12
48	1	13
49	1	14
50	1	15
51	1	16
52	1	17
53	1	18
54	1	19
55	1	20
56	1	21
57	1	22
58	1	23
59	1	24
60	1	25
61	1	26
62	1	27
63	1	28
64	1	29
65	1	30
66	1	31
67	1	32
68	1	33
69	1	34
70	1	35
71	1	36
72	1	37
73	1	38
74	1	39
75	1	40
76	1	41
77	1	42
78	1	43
79	1	44
80	1	45
81	1	46
82	1	47
83	1	48
84	1	49
85	1	50
86	1	51
87	1	52
88	1	53
89	1	54
90	1	55
91	1	56
92	1	57
93	1	58
94	1	59
95	1	60
96	1	61
97	1	62
98	1	63
99	1	64
100	1	65
101	1	66
102	1	67
103	1	68
104	1	69
105	1	70
106	1	71
107	1	72
108	1	73
109	1	74
110	1	75
111	1	76
112	1	77
113	1	78
114	1	79
115	1	80
116	1	81
117	1	82
118	1	83
119	1	84
120	1	85
121	5	1
122	5	2
123	5	3
124	5	4
125	5	5
126	5	6
127	5	7
128	5	8
129	5	9
130	5	10
131	5	11
132	5	12
133	5	13
134	5	14
135	5	15
136	5	16
137	5	17
138	5	18
139	5	19
140	5	20
141	5	21
142	5	22
143	5	23
144	5	24
145	5	25
146	5	26
147	5	27
148	5	28
149	5	29
150	5	30
151	5	31
152	5	32
153	5	33
154	5	34
155	5	35
156	5	36
157	5	37
158	5	38
159	5	39
160	5	40
161	5	41
162	5	42
163	5	43
164	5	44
165	5	45
166	5	46
167	5	47
168	5	48
169	5	49
170	5	50
171	5	51
172	5	52
173	5	53
174	5	54
175	5	55
176	5	56
177	5	57
178	5	58
179	5	59
180	5	60
181	5	61
182	5	62
183	5	63
184	5	64
185	5	65
186	5	66
187	5	67
188	5	68
189	5	69
190	5	70
191	5	71
192	5	72
193	5	73
194	5	74
195	5	75
196	5	76
197	5	77
198	5	78
199	5	79
200	5	80
201	5	81
202	5	82
203	5	83
204	5	84
205	5	85
206	2	86
207	3	87
328	1	86
329	1	87
415	5	86
416	5	87
420	2	88
421	3	88
422	4	89
545	1	88
546	1	89
634	5	88
635	5	89
636	1	90
637	1	91
639	1	92
640	1	93
641	1	94
642	1	95
643	1	96
644	1	97
653	1	98
654	1	99
655	1	100
656	1	101
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add job	2	add_job
6	Can change job	2	change_job
7	Can delete job	2	delete_job
8	Can view job	2	view_job
9	Can set Job status Pending for Approval	2	can_set_pending_for_approval_job
10	Can set Archive Jobs	2	can_archive_jobs
11	Can set Restore Jobs	2	can_restore_jobs
12	Can add Service Ticket	3	add_serviceticket
13	Can change Service Ticket	3	change_serviceticket
14	Can delete Service Ticket	3	delete_serviceticket
15	Can view Service Ticket	3	view_serviceticket
16	Can set Service Ticket status Pending for Approval	3	can_set_pending_for_approval_service_ticket
17	Add mechanic to the Service Ticket	3	add_mechanic_to_service_ticket
18	Can approve Service Ticket	3	can_approve_service_ticket
19	Can reject Service Ticket	3	can_reject_service_ticket
20	Can add customer	4	add_customer
21	Can change customer	4	change_customer
22	Can delete customer	4	delete_customer
23	Can view customer	4	view_customer
24	Can add location	5	add_location
25	Can change location	5	change_location
26	Can delete location	5	delete_location
27	Can view location	5	view_location
28	Can add settings	6	add_settings
29	Can change settings	6	change_settings
30	Can delete settings	6	delete_settings
31	Can view settings	6	view_settings
32	Can add employee work block	7	add_employeeworkblock
33	Can change employee work block	7	change_employeeworkblock
34	Can delete employee work block	7	delete_employeeworkblock
35	Can view employee work block	7	view_employeeworkblock
36	Can add attachment	8	add_attachment
37	Can change attachment	8	change_attachment
38	Can delete attachment	8	delete_attachment
39	Can view attachment	8	view_attachment
40	Can add db lock date	9	add_dblockdate
41	Can change db lock date	9	change_dblockdate
42	Can delete db lock date	9	delete_dblockdate
43	Can view db lock date	9	view_dblockdate
44	Can add log entry	10	add_logentry
45	Can change log entry	10	change_logentry
46	Can delete log entry	10	delete_logentry
47	Can view log entry	10	view_logentry
48	Can add permission	11	add_permission
49	Can change permission	11	change_permission
50	Can delete permission	11	delete_permission
51	Can view permission	11	view_permission
52	Can add group	12	add_group
53	Can change group	12	change_group
54	Can delete group	12	delete_group
55	Can view group	12	view_group
56	Can add user	13	add_user
57	Can change user	13	change_user
58	Can delete user	13	delete_user
59	Can view user	13	view_user
60	Can add Admin	14	add_admin
61	Can change Admin	14	change_admin
62	Can delete Admin	14	delete_admin
63	Can view Admin	14	view_admin
64	Can add Biller	15	add_biller
65	Can change Biller	15	change_biller
66	Can delete Biller	15	delete_biller
67	Can view Biller	15	view_biller
68	Can add Manager	16	add_manager
69	Can change Manager	16	change_manager
70	Can delete Manager	16	delete_manager
71	Can view Manager	16	view_manager
72	Can add Mechanic	17	add_mechanic
73	Can change Mechanic	17	change_mechanic
74	Can delete Mechanic	17	delete_mechanic
75	Can view Mechanic	17	view_mechanic
76	Can add content type	18	add_contenttype
77	Can change content type	18	change_contenttype
78	Can delete content type	18	delete_contenttype
79	Can view content type	18	view_contenttype
80	Can add Indirect Hours	19	add_indirecthours
81	Can change Indirect Hours	19	change_indirecthours
82	Can delete Indirect Hours	19	delete_indirecthours
83	Can view Indirect Hours	19	view_indirecthours
84	Can approve Indirect Hours	19	can_approve_indirect_hours
85	Can reject Indirect Hours	19	can_reject_indirect_hours
86		15	can_set_pending_for_approval
87		16	can_set_pending_for_approval
88		13	can_get_reports
89		17	can_get_time_reports
90		13	can_archive_users
91		13	can_restore_users
92		20	add_action
93		20	view_action
94		20	change_action
95		20	delete_action
96		19	can_archive_indirect_hours
97		19	can_restore_indirect_hours
98		21	add_timecode
99		21	view_timecode
100		21	change_timecode
101		21	delete_timecode
102	Can add session	22	add_session
103	Can change session	22	change_session
104	Can delete session	22	delete_session
105	Can view session	22	view_session
106	Can set Archive Users	14	can_archive_users
107	Can set Restore Users	14	can_restore_users
108	Can get Reports	14	can_get_reports
109	Can editing approved service tickets	14	can_editing_approved_st
110	Can add Superuser	23	add_superuser
111	Can change Superuser	23	change_superuser
112	Can delete Superuser	23	delete_superuser
113	Can view Superuser	23	view_superuser
114	Can add blacklisted token	24	add_blacklistedtoken
115	Can change blacklisted token	24	change_blacklistedtoken
116	Can delete blacklisted token	24	delete_blacklistedtoken
117	Can view blacklisted token	24	view_blacklistedtoken
\.


--
-- Data for Name: authentication_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.authentication_user (id, password, last_login, is_superuser, first_name, last_name, email, date_joined, is_staff, is_confirmed_email, status, sent_email_notifications, sent_push_notifications, manager_id) FROM stdin;
2	pbkdf2_sha256$260000$XBzXaTSb8XnKC15AJCVLoO$WJB+quOCgmb8N1hPhLrl2ezKsFl5M/vBxrxBgKC6Ps4=	\N	f	Arslan	Manager	arslan@gmail.com	2024-05-14 12:56:15.523932+05	t	f	1	t	t	\N
3	pbkdf2_sha256$260000$1TRfMJOHmRP74TfePus1GL$Zz1OH/VpQ4yUVbze+ge8ysgWnU+1HJJ+Dfa+0YSL+0s=	\N	f	Majid	Mechanic	majid@gmail.com	2024-05-14 12:56:55.836461+05	t	f	1	t	t	2
1	pbkdf2_sha256$260000$LKpJlFzCD16r7VXFEh8SwZ$rexTTc1mC/FXFTDTmZo1Xx2FGzU2DM/Fx+eZ3jXsYYU=	2024-05-16 14:38:16.650327+05	t			admin@gmail.com	2024-05-14 12:48:37.649085+05	t	f	1	t	t	\N
\.


--
-- Data for Name: authentication_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.authentication_user_groups (id, user_id, group_id) FROM stdin;
1	1	1
2	2	3
3	3	4
\.


--
-- Data for Name: authentication_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.authentication_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: blacklist_blacklistedtoken; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.blacklist_blacklistedtoken (id, token, expires_at, blacklisted_at, user_id, token_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2024-05-14 15:02:47.309653+05	1	1244	1	[{"added": {}}]	21	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	api	job
3	api	serviceticket
4	api	customer
5	api	location
6	api	settings
7	api	employeeworkblock
8	api	attachment
9	api	dblockdate
10	auditlog	logentry
11	auth	permission
12	auth	group
13	authentication	user
14	authentication	admin
15	authentication	biller
16	authentication	manager
17	authentication	mechanic
18	contenttypes	contenttype
19	time_tracker	indirecthours
20	notifications	action
21	time_tracker	timecode
22	sessions	session
23	authentication	superuser
24	blacklist	blacklistedtoken
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2024-05-14 12:47:57.754505+05
2	contenttypes	0002_remove_content_type_name	2024-05-14 12:47:57.779505+05
3	auth	0001_initial	2024-05-14 12:47:57.89105+05
4	auth	0002_alter_permission_name_max_length	2024-05-14 12:47:57.902056+05
5	auth	0003_alter_user_email_max_length	2024-05-14 12:47:57.913047+05
6	auth	0004_alter_user_username_opts	2024-05-14 12:47:57.925048+05
7	auth	0005_alter_user_last_login_null	2024-05-14 12:47:57.945057+05
8	auth	0006_require_contenttypes_0002	2024-05-14 12:47:57.949065+05
9	auth	0007_alter_validators_add_error_messages	2024-05-14 12:47:57.961582+05
10	auth	0008_alter_user_username_max_length	2024-05-14 12:47:57.975579+05
11	auth	0009_alter_user_last_name_max_length	2024-05-14 12:47:57.990581+05
12	auth	0010_alter_group_name_max_length	2024-05-14 12:47:58.008581+05
13	auth	0011_update_proxy_permissions	2024-05-14 12:47:58.024582+05
14	authentication	0001_initial	2024-05-14 12:47:58.148188+05
15	admin	0001_initial	2024-05-14 12:47:58.200711+05
16	admin	0002_logentry_remove_auto_add	2024-05-14 12:47:58.221707+05
17	admin	0003_logentry_add_action_flag_choices	2024-05-14 12:47:58.24572+05
18	api	0001_initial	2024-05-14 12:47:58.307311+05
19	api	0002_auto_20191127_1809	2024-05-14 12:47:58.398882+05
20	api	0003_auto_20191128_1541	2024-05-14 12:47:58.478405+05
21	api	0002_auto_20191129_1227	2024-05-14 12:47:58.674526+05
22	api	0004_merge_20191129_1348	2024-05-14 12:47:58.678528+05
23	api	0005_remove_serviceticket_customer	2024-05-14 12:47:58.717526+05
24	api	0006_add_citext_ppostgress_support	2024-05-14 12:47:58.821084+05
25	api	0007_auto_20191203_1541	2024-05-14 12:47:58.871601+05
26	api	0008_merge_20191205_1140	2024-05-14 12:47:58.881602+05
27	api	0008_auto_20191204_1524	2024-05-14 12:47:58.9346+05
28	api	0009_merge_20191205_1248	2024-05-14 12:47:58.938616+05
29	api	0011_auto_20191209_1539	2024-05-14 12:47:59.050647+05
30	api	0012_auto_20191211_1427	2024-05-14 12:47:59.117658+05
31	api	0012_auto_20191211_1247	2024-05-14 12:47:59.149672+05
32	api	0013_merge_20191212_0941	2024-05-14 12:47:59.153798+05
33	api	0012_auto_20191211_1551	2024-05-14 12:47:59.292822+05
34	api	0014_merge_20191212_1035	2024-05-14 12:47:59.305502+05
35	api	0015_auto_20191212_1513	2024-05-14 12:47:59.36795+05
36	api	0016_settings	2024-05-14 12:47:59.38415+05
37	api	0017_create_settings_instance	2024-05-14 12:47:59.425262+05
38	api	0018_auto_20191220_1419	2024-05-14 12:48:00.90291+05
39	api	0019_auto_20191227_1415	2024-05-14 12:48:01.034435+05
40	api	0020_auto_20200109_1310	2024-05-14 12:48:01.11396+05
41	api	0020_attachment	2024-05-14 12:48:01.164491+05
42	api	0021_merge_20200110_1643	2024-05-14 12:48:01.168497+05
43	api	0022_serviceticket_reject_description	2024-05-14 12:48:01.204488+05
44	api	0023_auto_20200123_1247	2024-05-14 12:48:01.244497+05
45	api	0023_auto_20200122_1401	2024-05-14 12:48:01.328018+05
46	api	0024_merge_20200124_1404	2024-05-14 12:48:01.332016+05
47	api	0024_merge_20200124_1327	2024-05-14 12:48:01.337018+05
48	api	0025_merge_20200124_1429	2024-05-14 12:48:01.341034+05
49	api	0022_auto_20200115_1356	2024-05-14 12:48:01.393071+05
50	api	0026_merge_20200129_1617	2024-05-14 12:48:01.396067+05
51	api	0023_auto_20200116_1511	2024-05-14 12:48:01.459174+05
52	api	0024_merge_20200124_1259	2024-05-14 12:48:01.463171+05
53	api	0026_merge_20200124_1552	2024-05-14 12:48:01.467174+05
54	api	0027_merge_20200131_1424	2024-05-14 12:48:01.472174+05
55	api	0027_auto_20200130_1638	2024-05-14 12:48:01.539185+05
56	api	0028_merge_20200131_1551	2024-05-14 12:48:01.543185+05
57	api	0029_auto_20200204_1036	2024-05-14 12:48:01.584175+05
58	api	0030_auto_20200213_1327	2024-05-14 12:48:01.751244+05
59	api	0031_ST_employee	2024-05-14 12:48:01.785762+05
60	api	0032_auto_20200330_1700	2024-05-14 12:48:01.829778+05
61	api	0033_auto_20200213_13270	2024-05-14 12:48:01.933973+05
62	api	0034_auto_20200401_1644	2024-05-14 12:48:01.949979+05
63	api	0031_remove_serviceticket_kandr_wo	2024-05-14 12:48:01.974507+05
64	api	0032_auto_20200324_1154	2024-05-14 12:48:02.057026+05
65	api	0035_merge_20200407_1437	2024-05-14 12:48:02.060025+05
66	api	0036_auto_20200626_1157	2024-05-14 12:48:02.095022+05
67	api	0037_auto_20201015_1618	2024-05-14 12:48:02.137029+05
68	api	0038_auto_20201015_1800	2024-05-14 12:48:02.209145+05
69	api	0039_employee_work_dates	2024-05-14 12:48:02.253159+05
70	api	0040_dblockdate	2024-05-14 12:48:02.268677+05
71	api	0041_auto_20230324_1647	2024-05-14 12:48:02.361199+05
72	api	0042_auto_20240108_1850	2024-05-14 12:48:02.442223+05
73	auditlog	0001_initial	2024-05-14 12:48:02.522723+05
74	auditlog	0002_auto_support_long_primary_keys	2024-05-14 12:48:02.609245+05
75	auditlog	0003_logentry_remote_addr	2024-05-14 12:48:02.656773+05
76	auditlog	0004_logentry_detailed_object_repr	2024-05-14 12:48:02.702803+05
77	auditlog	0005_logentry_additional_data_verbose_name	2024-05-14 12:48:02.743782+05
78	auditlog	0006_object_pk_index	2024-05-14 12:48:02.826314+05
79	auditlog	0007_object_pk_type	2024-05-14 12:48:02.870828+05
80	auditlog	0008_action_index	2024-05-14 12:48:02.912829+05
81	auditlog	0009_alter_logentry_additional_data	2024-05-14 12:48:02.955368+05
82	auditlog	0010_alter_logentry_timestamp	2024-05-14 12:48:03.001408+05
83	auth	0012_alter_user_first_name_max_length	2024-05-14 12:48:03.022369+05
84	time_tracker	0001_initial	2024-05-14 12:48:03.08889+05
85	time_tracker	0002_auto_20200106_1242	2024-05-14 12:48:03.26252+05
86	authentication	0002_create_default_groups	2024-05-14 12:48:03.294522+05
87	authentication	0003_create_default_permissions	2024-05-14 12:48:03.49089+05
88	authentication	0004_update_group_permissions0	2024-05-14 12:48:03.655987+05
89	authentication	0005_auto_20191129_1349	2024-05-14 12:48:03.730987+05
90	authentication	0006_auto_20191129_1410	2024-05-14 12:48:03.778512+05
91	authentication	0009_add_first_user_to_admin_group	2024-05-14 12:48:03.841969+05
92	authentication	0007_auto_20191202_1407	2024-05-14 12:48:03.887146+05
93	authentication	0008_add_custom_permissions_to_biller_and_manager_models	2024-05-14 12:48:03.967303+05
94	authentication	0010_merge_20191205_1140	2024-05-14 12:48:03.972331+05
95	authentication	0011_auto_20191211_1247	2024-05-14 12:48:04.041141+05
96	authentication	0012_superuser	2024-05-14 12:48:04.048145+05
97	authentication	0013_update_permissions_for_service_ticket	2024-05-14 12:48:04.203752+05
98	authentication	0014_user_status	2024-05-14 12:48:04.234751+05
99	authentication	0015_change_user_roles_order_in_db	2024-05-14 12:48:04.293274+05
100	authentication	0016_auto_20200115_1259	2024-05-14 12:48:04.344286+05
101	authentication	0017_user_sent_email_notifications	2024-05-14 12:48:04.384827+05
102	authentication	0018_change_job_permission	2024-05-14 12:48:04.435833+05
103	authentication	0019_auto_20200204_1036	2024-05-14 12:48:04.462938+05
104	authentication	0020_auto_20200211_1449	2024-05-14 12:48:04.521942+05
105	authentication	0021_auto_20200320_1641	2024-05-14 12:48:04.609063+05
106	authentication	0021_auto_20200319_1252	2024-05-14 12:48:04.641076+05
107	authentication	0022_merge_20200324_1426	2024-05-14 12:48:04.645074+05
108	authentication	0022_merge_20200324_1318	2024-05-14 12:48:04.650076+05
109	authentication	0023_merge_20200401_1051	2024-05-14 12:48:04.653078+05
110	authentication	0021_user_sent_push_notifications	2024-05-14 12:48:04.698177+05
111	authentication	0024_merge_20200407_1437	2024-05-14 12:48:04.703174+05
112	authentication	0023_merge_20200407_1442	2024-05-14 12:48:04.707177+05
113	authentication	0025_merge_20200408_0939	2024-05-14 12:48:04.714175+05
114	authentication	0026_add_permission_can_get_time_report_for_mech	2024-05-14 12:48:04.771713+05
115	authentication	0027_user_manager	2024-05-14 12:48:04.83871+05
116	blacklist	0001_initial	2024-05-14 12:48:04.926238+05
117	blacklist	0002_add_token_id	2024-05-14 12:48:05.145858+05
118	notifications	0001_initial	2024-05-14 12:48:05.235376+05
119	notifications	0002_action_is_viewed	2024-05-14 12:48:05.278451+05
120	notifications	0003_auto_20200120_1647	2024-05-14 12:48:05.331457+05
121	notifications	0004_auto_20200520_1616	2024-05-14 12:48:05.39548+05
122	sessions	0001_initial	2024-05-14 12:48:05.425482+05
123	time_tracker	0003_auto_20200106_1311	2024-05-14 12:48:05.582722+05
124	time_tracker	0004_auto_20200106_1531	2024-05-14 12:48:05.610718+05
125	time_tracker	0005_auto_20200106_1532	2024-05-14 12:48:05.653728+05
126	time_tracker	0006_auto_20200115_1002	2024-05-14 12:48:05.785762+05
127	time_tracker	0007_indirecthours_is_archive	2024-05-14 12:48:05.810765+05
128	time_tracker	0008_auto_20200204_1036	2024-05-14 12:48:05.85377+05
129	time_tracker	0009_update_admin_group_perms	2024-05-14 12:48:05.96398+05
130	time_tracker	0010_auto_20200206_1546	2024-05-14 12:48:06.100281+05
131	time_tracker	0011_auto_20200226_1649	2024-05-14 12:48:06.166506+05
132	time_tracker	0012_auto_20200319_1252	2024-05-14 12:48:06.22304+05
133	time_tracker	0012_auto_20200313_1531	2024-05-14 12:48:06.310055+05
134	time_tracker	0013_merge_20200319_1417	2024-05-14 12:48:06.315064+05
135	time_tracker	0012_auto_20200318_1525	2024-05-14 12:48:06.362572+05
136	time_tracker	0014_merge_20200324_1426	2024-05-14 12:48:06.369573+05
137	time_tracker	0014_merge_20200324_1318	2024-05-14 12:48:06.37259+05
138	time_tracker	0015_merge_20200401_1051	2024-05-14 12:48:06.375577+05
139	time_tracker	0013_auto_20200521_2108	2024-05-14 12:48:06.434576+05
140	time_tracker	0016_merge_20200522_1458	2024-05-14 12:48:06.438575+05
141	time_tracker	0017_auto_20240207_1745	2024-05-14 12:48:06.654206+05
142	time_tracker	0018_rename_mechanic_indirecthours_mechanic_old	2024-05-14 12:48:06.683731+05
143	time_tracker	0019_auto_20240207_1747	2024-05-14 12:48:06.780259+05
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
\.


--
-- Data for Name: notifications_action; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.notifications_action (id, creation_date, update_date, object_type, connected_object_id, description, is_viewed) FROM stdin;
1	2024-05-14	2024-05-14	0	1	You have been assigned to the Job - "1"	f
2	2024-05-14	2024-05-14	0	1	You have been assigned to the Job - "1"	f
3	2024-05-14	2024-05-14	0	1	Job "1" created successfully	f
4	2024-05-14	2024-05-14	0	2	You have been assigned to the Job - "a12"	f
5	2024-05-14	2024-05-14	0	2	You have been assigned to the Job - "a12"	f
6	2024-05-14	2024-05-14	0	2	Job "a12" created successfully	f
7	2024-05-14	2024-05-14	0	3	You have been assigned to the Job - "3"	f
8	2024-05-14	2024-05-14	0	3	You have been assigned to the Job - "3"	f
9	2024-05-14	2024-05-14	0	3	Job "3" created successfully	f
10	2024-05-14	2024-05-14	0	4	You have been assigned to the Job - "5"	f
11	2024-05-14	2024-05-14	0	4	You have been assigned to the Job - "5"	f
12	2024-05-14	2024-05-14	0	5	You have been assigned to the Job - "2404-34366-PA4-4-UNIT 2295 SHOP MAKE READY"	f
13	2024-05-14	2024-05-14	0	5	You have been assigned to the Job - "2404-34366-PA4-4-UNIT 2295 SHOP MAKE READY"	f
14	2024-05-14	2024-05-14	0	6	You have been assigned to the Job - "2405-34810-OK7-WALMART 121 PLANNED PPO"	f
15	2024-05-14	2024-05-14	0	6	You have been assigned to the Job - "2405-34810-OK7-WALMART 121 PLANNED PPO"	f
16	2024-05-14	2024-05-14	0	7	You have been assigned to the Job - "2404-34131-LA7-GENERATOR TESTING"	f
17	2024-05-14	2024-05-14	0	7	You have been assigned to the Job - "2404-34131-LA7-GENERATOR TESTING"	f
18	2024-05-14	2024-05-14	2	1	"2.00" Indirect Hours have been Submitted for - "Majid Mechanic"	f
19	2024-05-15	2024-05-15	1	1	The Service Ticket - "1" for the Job - "1" has been Submitted for Approval	f
20	2024-05-15	2024-05-15	1	1	The Service Ticket - "1" for the Job - "1" has been Approved	f
21	2024-05-15	2024-05-15	1	3	The Service Ticket - "3" for the Job - "5" has been Submitted for Approval	f
22	2024-05-15	2024-05-15	1	2	The Service Ticket - "2" for the Job - "a12" has been Submitted for Approval	f
23	2024-05-15	2024-05-15	1	4	The Service Ticket - "4" for the Job - "2404-34366-PA4-4-UNIT 2295 SHOP MAKE READY" has been Submitted for Approval	f
24	2024-05-15	2024-05-15	1	5	The Service Ticket - "5" for the Job - "2404-34366-PA4-4-UNIT 2295 SHOP MAKE READY" has been Submitted for Approval	f
25	2024-05-15	2024-05-15	1	6	The Service Ticket - "6" for the Job - "2404-34131-LA7-GENERATOR TESTING" has been Submitted for Approval	f
26	2024-05-15	2024-05-15	1	7	The Service Ticket - "7" for the Job - "2405-34810-OK7-WALMART 121 PLANNED PPO" has been Submitted for Approval	f
27	2024-05-15	2024-05-15	1	8	The Service Ticket - "8" for the Job - "2404-34366-PA4-4-UNIT 2295 SHOP MAKE READY" has been Submitted for Approval	f
28	2024-05-15	2024-05-15	2	2	"12.00" Indirect Hours have been Submitted for - "Majid Mechanic"	f
29	2024-05-16	2024-05-16	2	3	"24.00" Indirect Hours have been Submitted for - "Majid Mechanic"	f
30	2024-05-16	2024-05-16	2	4	"24.00" Indirect Hours have been Submitted for - "Majid Mechanic"	f
31	2024-05-16	2024-05-16	1	9	The Service Ticket - "9" for the Job - "2404-34131-LA7-GENERATOR TESTING" has been Submitted for Approval	f
\.


--
-- Data for Name: notifications_action_connected_users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.notifications_action_connected_users (id, action_id, user_id) FROM stdin;
1	1	3
2	2	2
3	3	1
4	4	3
5	5	2
6	6	1
7	7	3
8	8	2
9	9	1
10	10	3
11	11	2
12	12	3
13	13	2
14	14	3
15	15	2
16	16	3
17	17	2
18	18	2
19	19	2
20	19	3
21	20	3
22	21	2
23	21	3
24	22	2
25	22	3
26	23	2
27	23	3
28	24	2
29	24	3
30	25	2
31	25	3
32	26	2
33	26	3
34	27	2
35	27	3
36	28	2
37	29	2
38	30	2
39	31	2
40	31	3
\.


--
-- Data for Name: time_tracker_indirecthours; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.time_tracker_indirecthours (id, creation_date, update_date, date, hours, time_code_id, notes, status, is_archive) FROM stdin;
1	2024-05-14	2024-05-14	2024-05-14	2.00	1	Testing	1	f
2	2024-05-15	2024-05-15	2024-05-15	12.00	1	good	1	f
3	2024-05-16	2024-05-16	2024-05-16	24.00	1	Testing from mobile	1	f
4	2024-05-16	2024-05-16	2024-05-16	24.00	1	Offline Testing	1	f
\.


--
-- Data for Name: time_tracker_indirecthours_mechanic; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.time_tracker_indirecthours_mechanic (id, indirecthours_id, mechanic_id) FROM stdin;
1	1	3
2	2	3
3	3	3
4	4	3
\.


--
-- Data for Name: time_tracker_timecode; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.time_tracker_timecode (id, name) FROM stdin;
1	1244
\.


--
-- Name: api_attachment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.api_attachment_id_seq', 1, false);


--
-- Name: api_customer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.api_customer_id_seq', 1, true);


--
-- Name: api_customer_locations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.api_customer_locations_id_seq', 1, true);


--
-- Name: api_dblockdate_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.api_dblockdate_id_seq', 1, true);


--
-- Name: api_employeeworkblock_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.api_employeeworkblock_id_seq', 10, true);


--
-- Name: api_job_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.api_job_id_seq', 7, true);


--
-- Name: api_job_managers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.api_job_managers_id_seq', 7, true);


--
-- Name: api_job_mechanics_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.api_job_mechanics_id_seq', 7, true);


--
-- Name: api_location_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.api_location_id_seq', 1, true);


--
-- Name: api_serviceticket_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.api_serviceticket_id_seq', 9, true);


--
-- Name: api_settings_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.api_settings_id_seq', 1, true);


--
-- Name: auditlog_logentry_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auditlog_logentry_id_seq', 31, true);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 5, true);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 656, true);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 117, true);


--
-- Name: authentication_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.authentication_user_groups_id_seq', 3, true);


--
-- Name: authentication_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.authentication_user_id_seq', 3, true);


--
-- Name: authentication_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.authentication_user_user_permissions_id_seq', 1, false);


--
-- Name: blacklist_blacklistedtoken_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.blacklist_blacklistedtoken_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 24, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 143, true);


--
-- Name: notifications_action_connected_users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.notifications_action_connected_users_id_seq', 40, true);


--
-- Name: notifications_action_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.notifications_action_id_seq', 31, true);


--
-- Name: time_tracker_indirecthours_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.time_tracker_indirecthours_id_seq', 4, true);


--
-- Name: time_tracker_indirecthours_mechanic_new_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.time_tracker_indirecthours_mechanic_new_id_seq', 4, true);


--
-- Name: time_tracker_timecode_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.time_tracker_timecode_id_seq', 1, true);


--
-- Name: api_attachment api_attachment_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_attachment
    ADD CONSTRAINT api_attachment_pkey PRIMARY KEY (id);


--
-- Name: api_customer_locations api_customer_locations_customer_id_location_id_04c1d656_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_customer_locations
    ADD CONSTRAINT api_customer_locations_customer_id_location_id_04c1d656_uniq UNIQUE (customer_id, location_id);


--
-- Name: api_customer_locations api_customer_locations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_customer_locations
    ADD CONSTRAINT api_customer_locations_pkey PRIMARY KEY (id);


--
-- Name: api_customer api_customer_name_2f51cc5a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_customer
    ADD CONSTRAINT api_customer_name_2f51cc5a_uniq UNIQUE (name);


--
-- Name: api_customer api_customer_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_customer
    ADD CONSTRAINT api_customer_pkey PRIMARY KEY (id);


--
-- Name: api_dblockdate api_dblockdate_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_dblockdate
    ADD CONSTRAINT api_dblockdate_pkey PRIMARY KEY (id);


--
-- Name: api_employeeworkblock api_employeeworkblock_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_employeeworkblock
    ADD CONSTRAINT api_employeeworkblock_pkey PRIMARY KEY (id);


--
-- Name: api_job_managers api_job_managers_job_id_manager_id_04fd47a7_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_job_managers
    ADD CONSTRAINT api_job_managers_job_id_manager_id_04fd47a7_uniq UNIQUE (job_id, manager_id);


--
-- Name: api_job_managers api_job_managers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_job_managers
    ADD CONSTRAINT api_job_managers_pkey PRIMARY KEY (id);


--
-- Name: api_job_mechanics api_job_mechanics_job_id_mechanic_id_b1519190_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_job_mechanics
    ADD CONSTRAINT api_job_mechanics_job_id_mechanic_id_b1519190_uniq UNIQUE (job_id, mechanic_id);


--
-- Name: api_job_mechanics api_job_mechanics_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_job_mechanics
    ADD CONSTRAINT api_job_mechanics_pkey PRIMARY KEY (id);


--
-- Name: api_job api_job_number_275f6eb1_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_job
    ADD CONSTRAINT api_job_number_275f6eb1_uniq UNIQUE (number);


--
-- Name: api_job api_job_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_job
    ADD CONSTRAINT api_job_pkey PRIMARY KEY (id);


--
-- Name: api_location api_location_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_location
    ADD CONSTRAINT api_location_name_key UNIQUE (name);


--
-- Name: api_location api_location_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_location
    ADD CONSTRAINT api_location_pkey PRIMARY KEY (id);


--
-- Name: api_serviceticket api_serviceticket_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_serviceticket
    ADD CONSTRAINT api_serviceticket_pkey PRIMARY KEY (id);


--
-- Name: api_settings api_settings_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_settings
    ADD CONSTRAINT api_settings_pkey PRIMARY KEY (id);


--
-- Name: auditlog_logentry auditlog_logentry_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auditlog_logentry
    ADD CONSTRAINT auditlog_logentry_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: authentication_user authentication_user_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authentication_user
    ADD CONSTRAINT authentication_user_email_key UNIQUE (email);


--
-- Name: authentication_user_groups authentication_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authentication_user_groups
    ADD CONSTRAINT authentication_user_groups_pkey PRIMARY KEY (id);


--
-- Name: authentication_user_groups authentication_user_groups_user_id_group_id_8af031ac_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authentication_user_groups
    ADD CONSTRAINT authentication_user_groups_user_id_group_id_8af031ac_uniq UNIQUE (user_id, group_id);


--
-- Name: authentication_user authentication_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authentication_user
    ADD CONSTRAINT authentication_user_pkey PRIMARY KEY (id);


--
-- Name: authentication_user_user_permissions authentication_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authentication_user_user_permissions
    ADD CONSTRAINT authentication_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: authentication_user_user_permissions authentication_user_user_user_id_permission_id_ec51b09f_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authentication_user_user_permissions
    ADD CONSTRAINT authentication_user_user_user_id_permission_id_ec51b09f_uniq UNIQUE (user_id, permission_id);


--
-- Name: blacklist_blacklistedtoken blacklist_blacklistedtoken_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.blacklist_blacklistedtoken
    ADD CONSTRAINT blacklist_blacklistedtoken_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: notifications_action_connected_users notifications_action_con_action_id_user_id_d5e1c3ac_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notifications_action_connected_users
    ADD CONSTRAINT notifications_action_con_action_id_user_id_d5e1c3ac_uniq UNIQUE (action_id, user_id);


--
-- Name: notifications_action_connected_users notifications_action_connected_users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notifications_action_connected_users
    ADD CONSTRAINT notifications_action_connected_users_pkey PRIMARY KEY (id);


--
-- Name: notifications_action notifications_action_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notifications_action
    ADD CONSTRAINT notifications_action_pkey PRIMARY KEY (id);


--
-- Name: time_tracker_indirecthours_mechanic time_tracker_indirecthou_indirecthours_id_mechani_ac35565d_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.time_tracker_indirecthours_mechanic
    ADD CONSTRAINT time_tracker_indirecthou_indirecthours_id_mechani_ac35565d_uniq UNIQUE (indirecthours_id, mechanic_id);


--
-- Name: time_tracker_indirecthours_mechanic time_tracker_indirecthours_mechanic_new_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.time_tracker_indirecthours_mechanic
    ADD CONSTRAINT time_tracker_indirecthours_mechanic_new_pkey PRIMARY KEY (id);


--
-- Name: time_tracker_indirecthours time_tracker_indirecthours_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.time_tracker_indirecthours
    ADD CONSTRAINT time_tracker_indirecthours_pkey PRIMARY KEY (id);


--
-- Name: time_tracker_timecode time_tracker_timecode_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.time_tracker_timecode
    ADD CONSTRAINT time_tracker_timecode_name_key UNIQUE (name);


--
-- Name: time_tracker_timecode time_tracker_timecode_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.time_tracker_timecode
    ADD CONSTRAINT time_tracker_timecode_pkey PRIMARY KEY (id);


--
-- Name: api_attachment_service_ticket_id_8a98fc20; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_attachment_service_ticket_id_8a98fc20 ON public.api_attachment USING btree (service_ticket_id);


--
-- Name: api_customer_locations_customer_id_49b64721; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_customer_locations_customer_id_49b64721 ON public.api_customer_locations USING btree (customer_id);


--
-- Name: api_customer_locations_location_id_93e0fba2; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_customer_locations_location_id_93e0fba2 ON public.api_customer_locations USING btree (location_id);


--
-- Name: api_employeeworkblock_employee_id_be5f8536; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_employeeworkblock_employee_id_be5f8536 ON public.api_employeeworkblock USING btree (employee_id);


--
-- Name: api_employeeworkblock_service_ticket_id_f33465bd; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_employeeworkblock_service_ticket_id_f33465bd ON public.api_employeeworkblock USING btree (service_ticket_id);


--
-- Name: api_job_approval_id_bf128859; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_job_approval_id_bf128859 ON public.api_job USING btree (approval_id);


--
-- Name: api_job_created_by_id_5b367c19; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_job_created_by_id_5b367c19 ON public.api_job USING btree (created_by_id);


--
-- Name: api_job_customer_id_9250d974; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_job_customer_id_9250d974 ON public.api_job USING btree (customer_id);


--
-- Name: api_job_location_id_e5328ffe; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_job_location_id_e5328ffe ON public.api_job USING btree (location_id);


--
-- Name: api_job_managers_job_id_6e7570b2; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_job_managers_job_id_6e7570b2 ON public.api_job_managers USING btree (job_id);


--
-- Name: api_job_managers_manager_id_0e3500f8; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_job_managers_manager_id_0e3500f8 ON public.api_job_managers USING btree (manager_id);


--
-- Name: api_job_mechanics_job_id_2592910e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_job_mechanics_job_id_2592910e ON public.api_job_mechanics USING btree (job_id);


--
-- Name: api_job_mechanics_mechanic_id_c006328b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_job_mechanics_mechanic_id_c006328b ON public.api_job_mechanics USING btree (mechanic_id);


--
-- Name: api_job_number_275f6eb1_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_job_number_275f6eb1_like ON public.api_job USING btree (number varchar_pattern_ops);


--
-- Name: api_job_requester_id_0aa1fc90; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_job_requester_id_0aa1fc90 ON public.api_job USING btree (requester_id);


--
-- Name: api_serviceticket_approval_id_c2ca092f; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_serviceticket_approval_id_c2ca092f ON public.api_serviceticket USING btree (approval_id);


--
-- Name: api_serviceticket_connected_job_id_86b9c96e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_serviceticket_connected_job_id_86b9c96e ON public.api_serviceticket USING btree (connected_job_id);


--
-- Name: api_serviceticket_created_by_id_6eaf13e0; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_serviceticket_created_by_id_6eaf13e0 ON public.api_serviceticket USING btree (created_by_id);


--
-- Name: api_serviceticket_requester_id_d1c37223; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_serviceticket_requester_id_d1c37223 ON public.api_serviceticket USING btree (requester_id);


--
-- Name: auditlog_logentry_action_229afe39; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auditlog_logentry_action_229afe39 ON public.auditlog_logentry USING btree (action);


--
-- Name: auditlog_logentry_actor_id_959271d2; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auditlog_logentry_actor_id_959271d2 ON public.auditlog_logentry USING btree (actor_id);


--
-- Name: auditlog_logentry_content_type_id_75830218; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auditlog_logentry_content_type_id_75830218 ON public.auditlog_logentry USING btree (content_type_id);


--
-- Name: auditlog_logentry_object_id_09c2eee8; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auditlog_logentry_object_id_09c2eee8 ON public.auditlog_logentry USING btree (object_id);


--
-- Name: auditlog_logentry_object_pk_6e3219c0; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auditlog_logentry_object_pk_6e3219c0 ON public.auditlog_logentry USING btree (object_pk);


--
-- Name: auditlog_logentry_object_pk_6e3219c0_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auditlog_logentry_object_pk_6e3219c0_like ON public.auditlog_logentry USING btree (object_pk varchar_pattern_ops);


--
-- Name: auditlog_logentry_timestamp_37867bb0; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auditlog_logentry_timestamp_37867bb0 ON public.auditlog_logentry USING btree ("timestamp");


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: authentication_user_email_2220eff5_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX authentication_user_email_2220eff5_like ON public.authentication_user USING btree (email varchar_pattern_ops);


--
-- Name: authentication_user_groups_group_id_6b5c44b7; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX authentication_user_groups_group_id_6b5c44b7 ON public.authentication_user_groups USING btree (group_id);


--
-- Name: authentication_user_groups_user_id_30868577; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX authentication_user_groups_user_id_30868577 ON public.authentication_user_groups USING btree (user_id);


--
-- Name: authentication_user_manager_id_8a07c1f5; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX authentication_user_manager_id_8a07c1f5 ON public.authentication_user USING btree (manager_id);


--
-- Name: authentication_user_user_permissions_permission_id_ea6be19a; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX authentication_user_user_permissions_permission_id_ea6be19a ON public.authentication_user_user_permissions USING btree (permission_id);


--
-- Name: authentication_user_user_permissions_user_id_736ebf7e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX authentication_user_user_permissions_user_id_736ebf7e ON public.authentication_user_user_permissions USING btree (user_id);


--
-- Name: blacklist_blacklistedtoken_expires_at_8ffda1c1; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX blacklist_blacklistedtoken_expires_at_8ffda1c1 ON public.blacklist_blacklistedtoken USING btree (expires_at);


--
-- Name: blacklist_blacklistedtoken_token_acbfdd7e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX blacklist_blacklistedtoken_token_acbfdd7e ON public.blacklist_blacklistedtoken USING btree (token);


--
-- Name: blacklist_blacklistedtoken_token_acbfdd7e_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX blacklist_blacklistedtoken_token_acbfdd7e_like ON public.blacklist_blacklistedtoken USING btree (token text_pattern_ops);


--
-- Name: blacklist_blacklistedtoken_token_id_aee3ed90; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX blacklist_blacklistedtoken_token_id_aee3ed90 ON public.blacklist_blacklistedtoken USING btree (token_id);


--
-- Name: blacklist_blacklistedtoken_user_id_e4068fb1; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX blacklist_blacklistedtoken_user_id_e4068fb1 ON public.blacklist_blacklistedtoken USING btree (user_id);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: notifications_action_connected_users_action_id_2db442a7; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX notifications_action_connected_users_action_id_2db442a7 ON public.notifications_action_connected_users USING btree (action_id);


--
-- Name: notifications_action_connected_users_user_id_6c7149a7; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX notifications_action_connected_users_user_id_6c7149a7 ON public.notifications_action_connected_users USING btree (user_id);


--
-- Name: time_tracker_indirecthours_indirecthours_id_42752488; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX time_tracker_indirecthours_indirecthours_id_42752488 ON public.time_tracker_indirecthours_mechanic USING btree (indirecthours_id);


--
-- Name: time_tracker_indirecthours_mechanic_new_mechanic_id_98aa4a21; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX time_tracker_indirecthours_mechanic_new_mechanic_id_98aa4a21 ON public.time_tracker_indirecthours_mechanic USING btree (mechanic_id);


--
-- Name: time_tracker_indirecthours_time_code_id_b89d5fca; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX time_tracker_indirecthours_time_code_id_b89d5fca ON public.time_tracker_indirecthours USING btree (time_code_id);


--
-- Name: time_tracker_timecode_name_d1d3e020_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX time_tracker_timecode_name_d1d3e020_like ON public.time_tracker_timecode USING btree (name varchar_pattern_ops);


--
-- Name: api_attachment api_attachment_service_ticket_id_8a98fc20_fk_api_servi; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_attachment
    ADD CONSTRAINT api_attachment_service_ticket_id_8a98fc20_fk_api_servi FOREIGN KEY (service_ticket_id) REFERENCES public.api_serviceticket(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_customer_locations api_customer_locations_customer_id_49b64721_fk_api_customer_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_customer_locations
    ADD CONSTRAINT api_customer_locations_customer_id_49b64721_fk_api_customer_id FOREIGN KEY (customer_id) REFERENCES public.api_customer(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_customer_locations api_customer_locations_location_id_93e0fba2_fk_api_location_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_customer_locations
    ADD CONSTRAINT api_customer_locations_location_id_93e0fba2_fk_api_location_id FOREIGN KEY (location_id) REFERENCES public.api_location(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_employeeworkblock api_employeeworkbloc_employee_id_be5f8536_fk_authentic; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_employeeworkblock
    ADD CONSTRAINT api_employeeworkbloc_employee_id_be5f8536_fk_authentic FOREIGN KEY (employee_id) REFERENCES public.authentication_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_employeeworkblock api_employeeworkbloc_service_ticket_id_f33465bd_fk_api_servi; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_employeeworkblock
    ADD CONSTRAINT api_employeeworkbloc_service_ticket_id_f33465bd_fk_api_servi FOREIGN KEY (service_ticket_id) REFERENCES public.api_serviceticket(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_job api_job_approval_id_bf128859_fk_authentication_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_job
    ADD CONSTRAINT api_job_approval_id_bf128859_fk_authentication_user_id FOREIGN KEY (approval_id) REFERENCES public.authentication_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_job api_job_created_by_id_5b367c19_fk_authentication_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_job
    ADD CONSTRAINT api_job_created_by_id_5b367c19_fk_authentication_user_id FOREIGN KEY (created_by_id) REFERENCES public.authentication_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_job api_job_customer_id_9250d974_fk_api_customer_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_job
    ADD CONSTRAINT api_job_customer_id_9250d974_fk_api_customer_id FOREIGN KEY (customer_id) REFERENCES public.api_customer(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_job api_job_location_id_e5328ffe_fk_api_location_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_job
    ADD CONSTRAINT api_job_location_id_e5328ffe_fk_api_location_id FOREIGN KEY (location_id) REFERENCES public.api_location(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_job_managers api_job_managers_job_id_6e7570b2_fk_api_job_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_job_managers
    ADD CONSTRAINT api_job_managers_job_id_6e7570b2_fk_api_job_id FOREIGN KEY (job_id) REFERENCES public.api_job(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_job_managers api_job_managers_manager_id_0e3500f8_fk_authentication_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_job_managers
    ADD CONSTRAINT api_job_managers_manager_id_0e3500f8_fk_authentication_user_id FOREIGN KEY (manager_id) REFERENCES public.authentication_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_job_mechanics api_job_mechanics_job_id_2592910e_fk_api_job_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_job_mechanics
    ADD CONSTRAINT api_job_mechanics_job_id_2592910e_fk_api_job_id FOREIGN KEY (job_id) REFERENCES public.api_job(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_job_mechanics api_job_mechanics_mechanic_id_c006328b_fk_authentic; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_job_mechanics
    ADD CONSTRAINT api_job_mechanics_mechanic_id_c006328b_fk_authentic FOREIGN KEY (mechanic_id) REFERENCES public.authentication_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_job api_job_requester_id_0aa1fc90_fk_authentication_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_job
    ADD CONSTRAINT api_job_requester_id_0aa1fc90_fk_authentication_user_id FOREIGN KEY (requester_id) REFERENCES public.authentication_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_serviceticket api_serviceticket_approval_id_c2ca092f_fk_authentic; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_serviceticket
    ADD CONSTRAINT api_serviceticket_approval_id_c2ca092f_fk_authentic FOREIGN KEY (approval_id) REFERENCES public.authentication_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_serviceticket api_serviceticket_connected_job_id_86b9c96e_fk_api_job_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_serviceticket
    ADD CONSTRAINT api_serviceticket_connected_job_id_86b9c96e_fk_api_job_id FOREIGN KEY (connected_job_id) REFERENCES public.api_job(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_serviceticket api_serviceticket_created_by_id_6eaf13e0_fk_authentic; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_serviceticket
    ADD CONSTRAINT api_serviceticket_created_by_id_6eaf13e0_fk_authentic FOREIGN KEY (created_by_id) REFERENCES public.authentication_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_serviceticket api_serviceticket_requester_id_d1c37223_fk_authentic; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_serviceticket
    ADD CONSTRAINT api_serviceticket_requester_id_d1c37223_fk_authentic FOREIGN KEY (requester_id) REFERENCES public.authentication_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auditlog_logentry auditlog_logentry_actor_id_959271d2_fk_authentication_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auditlog_logentry
    ADD CONSTRAINT auditlog_logentry_actor_id_959271d2_fk_authentication_user_id FOREIGN KEY (actor_id) REFERENCES public.authentication_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auditlog_logentry auditlog_logentry_content_type_id_75830218_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auditlog_logentry
    ADD CONSTRAINT auditlog_logentry_content_type_id_75830218_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authentication_user_user_permissions authentication_user__permission_id_ea6be19a_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authentication_user_user_permissions
    ADD CONSTRAINT authentication_user__permission_id_ea6be19a_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authentication_user_groups authentication_user__user_id_30868577_fk_authentic; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authentication_user_groups
    ADD CONSTRAINT authentication_user__user_id_30868577_fk_authentic FOREIGN KEY (user_id) REFERENCES public.authentication_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authentication_user_user_permissions authentication_user__user_id_736ebf7e_fk_authentic; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authentication_user_user_permissions
    ADD CONSTRAINT authentication_user__user_id_736ebf7e_fk_authentic FOREIGN KEY (user_id) REFERENCES public.authentication_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authentication_user_groups authentication_user_groups_group_id_6b5c44b7_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authentication_user_groups
    ADD CONSTRAINT authentication_user_groups_group_id_6b5c44b7_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authentication_user authentication_user_manager_id_8a07c1f5_fk_authentic; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authentication_user
    ADD CONSTRAINT authentication_user_manager_id_8a07c1f5_fk_authentic FOREIGN KEY (manager_id) REFERENCES public.authentication_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: blacklist_blacklistedtoken blacklist_blackliste_user_id_e4068fb1_fk_authentic; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.blacklist_blacklistedtoken
    ADD CONSTRAINT blacklist_blackliste_user_id_e4068fb1_fk_authentic FOREIGN KEY (user_id) REFERENCES public.authentication_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_authentication_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_authentication_user_id FOREIGN KEY (user_id) REFERENCES public.authentication_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: notifications_action_connected_users notifications_action_action_id_2db442a7_fk_notificat; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notifications_action_connected_users
    ADD CONSTRAINT notifications_action_action_id_2db442a7_fk_notificat FOREIGN KEY (action_id) REFERENCES public.notifications_action(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: notifications_action_connected_users notifications_action_user_id_6c7149a7_fk_authentic; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notifications_action_connected_users
    ADD CONSTRAINT notifications_action_user_id_6c7149a7_fk_authentic FOREIGN KEY (user_id) REFERENCES public.authentication_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: time_tracker_indirecthours_mechanic time_tracker_indirec_indirecthours_id_42752488_fk_time_trac; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.time_tracker_indirecthours_mechanic
    ADD CONSTRAINT time_tracker_indirec_indirecthours_id_42752488_fk_time_trac FOREIGN KEY (indirecthours_id) REFERENCES public.time_tracker_indirecthours(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: time_tracker_indirecthours_mechanic time_tracker_indirec_mechanic_id_98aa4a21_fk_authentic; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.time_tracker_indirecthours_mechanic
    ADD CONSTRAINT time_tracker_indirec_mechanic_id_98aa4a21_fk_authentic FOREIGN KEY (mechanic_id) REFERENCES public.authentication_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: time_tracker_indirecthours time_tracker_indirec_time_code_id_b89d5fca_fk_time_trac; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.time_tracker_indirecthours
    ADD CONSTRAINT time_tracker_indirec_time_code_id_b89d5fca_fk_time_trac FOREIGN KEY (time_code_id) REFERENCES public.time_tracker_timecode(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

