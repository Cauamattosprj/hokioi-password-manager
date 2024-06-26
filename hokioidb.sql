PGDMP      ,                |            hokioidb    16.3    16.3                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16407    hokioidb    DATABASE        CREATE DATABASE hokioidb WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Portuguese_Brazil.1252';
    DROP DATABASE hokioidb;
                postgres    false                        3079    16408 	   uuid-ossp 	   EXTENSION     ?   CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA public;
    DROP EXTENSION "uuid-ossp";
                   false                       0    0    EXTENSION "uuid-ossp"    COMMENT     W   COMMENT ON EXTENSION "uuid-ossp" IS 'generate universally unique identifiers (UUIDs)';
                        false    2            �            1259    16463    access_logs    TABLE     �   CREATE TABLE public.access_logs (
    id integer NOT NULL,
    user_id uuid,
    account_id uuid,
    accessed_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);
    DROP TABLE public.access_logs;
       public         heap    postgres    false            �            1259    16462    access_logs_id_seq    SEQUENCE     �   CREATE SEQUENCE public.access_logs_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.access_logs_id_seq;
       public          postgres    false    219                       0    0    access_logs_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.access_logs_id_seq OWNED BY public.access_logs.id;
          public          postgres    false    218            �            1259    16419    accounts    TABLE     L  CREATE TABLE public.accounts (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    account_name character varying(100),
    username character varying(100),
    password character varying(255),
    website_url character varying(255),
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    user_id uuid
);
    DROP TABLE public.accounts;
       public         heap    postgres    false    2            �            1259    16449    users    TABLE       CREATE TABLE public.users (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    username character varying(100),
    email character varying(255),
    password_hash character varying(255),
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);
    DROP TABLE public.users;
       public         heap    postgres    false    2            g           2604    16466    access_logs id    DEFAULT     p   ALTER TABLE ONLY public.access_logs ALTER COLUMN id SET DEFAULT nextval('public.access_logs_id_seq'::regclass);
 =   ALTER TABLE public.access_logs ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    218    219    219                      0    16463    access_logs 
   TABLE DATA           K   COPY public.access_logs (id, user_id, account_id, accessed_at) FROM stdin;
    public          postgres    false    219   x                 0    16419    accounts 
   TABLE DATA           j   COPY public.accounts (id, account_name, username, password, website_url, created_at, user_id) FROM stdin;
    public          postgres    false    216   �                 0    16449    users 
   TABLE DATA           O   COPY public.users (id, username, email, password_hash, created_at) FROM stdin;
    public          postgres    false    217   �                  0    0    access_logs_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.access_logs_id_seq', 1, false);
          public          postgres    false    218            r           2606    16469    access_logs access_logs_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.access_logs
    ADD CONSTRAINT access_logs_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.access_logs DROP CONSTRAINT access_logs_pkey;
       public            postgres    false    219            j           2606    16427    accounts accounts_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.accounts
    ADD CONSTRAINT accounts_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.accounts DROP CONSTRAINT accounts_pkey;
       public            postgres    false    216            l           2606    16461    users users_email_key 
   CONSTRAINT     Q   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);
 ?   ALTER TABLE ONLY public.users DROP CONSTRAINT users_email_key;
       public            postgres    false    217            n           2606    16457    users users_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public            postgres    false    217            p           2606    16459    users users_username_key 
   CONSTRAINT     W   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);
 B   ALTER TABLE ONLY public.users DROP CONSTRAINT users_username_key;
       public            postgres    false    217            t           2606    16475 '   access_logs access_logs_account_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.access_logs
    ADD CONSTRAINT access_logs_account_id_fkey FOREIGN KEY (account_id) REFERENCES public.accounts(id);
 Q   ALTER TABLE ONLY public.access_logs DROP CONSTRAINT access_logs_account_id_fkey;
       public          postgres    false    4714    219    216            u           2606    16470 $   access_logs access_logs_user_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.access_logs
    ADD CONSTRAINT access_logs_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);
 N   ALTER TABLE ONLY public.access_logs DROP CONSTRAINT access_logs_user_id_fkey;
       public          postgres    false    4718    219    217            s           2606    16480    accounts fk_accounts_user_id    FK CONSTRAINT     {   ALTER TABLE ONLY public.accounts
    ADD CONSTRAINT fk_accounts_user_id FOREIGN KEY (user_id) REFERENCES public.users(id);
 F   ALTER TABLE ONLY public.accounts DROP CONSTRAINT fk_accounts_user_id;
       public          postgres    false    4718    217    216                  x������ � �            x������ � �         c   x��A
�  �s�����ک�t�V� �.�>�6�q?WW�@d��T<$<T�fMB��+pJ���z6�n���~�=�	Fp	��藐D�D9�٬1�w#�     