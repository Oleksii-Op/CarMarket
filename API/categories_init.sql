CREATE TABLE IF NOT EXISTS public.categories
(                       --GENERATED ALWAYS AS IDENTITY NOT NULL
    category_id integer NOT NULL DEFAULT nextval('categories_category_id_seq'::regclass),
    category_name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    description character varying(255) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT categories_pkey PRIMARY KEY (category_id)
);

INSERT INTO categories (category_id, category_name, description)
VALUES(1, 'cars', 'This category represents cars driven by only combustion engines.');

INSERT INTO categories (category_id, category_name, description)
VALUES(2, 'trucks', 'This category represents trucks,heavy machinery.');

INSERT INTO categories (category_id, category_name, description)
VALUES(3, 'electrocars', 'This category represents cars driven by electrical motos.');

INSERT INTO categories (category_id, category_name, description)
VALUES(4, 'motorcycles', 'This category represents motorcycles.');