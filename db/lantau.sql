-- ----------------------------
-- Table structure for lantau
-- ----------------------------
DROP TABLE IF EXISTS "public"."lantau";
CREATE TABLE "public"."lantau" (
  "rid" int8 NOT NULL,
  "route" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "time" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "url" varchar(255) COLLATE "pg_catalog"."default"
)
;
ALTER TABLE "public"."lantau" OWNER TO "postgres";

-- ----------------------------
-- Records of lantau
-- ----------------------------
BEGIN;
INSERT INTO "public"."lantau" ("rid", "route", "time", "url") VALUES (1, 'Silvermine Bay Ferry Pier-->Nam Shan', '0.5 hr', 'https://1.bp.blogspot.com/-w-GbQB3Kd70/YA163RlennI/AAAAAAAADsI/e-cJpzgHOs07LIrIr-jERWsgBI5hgNuCACLcBGAsYHQ/w640-h480/01%25E6%25A2%2585%25E7%25AA%25A9.jpg');
INSERT INTO "public"."lantau" ("rid", "route", "time", "url") VALUES (2, 'Nam Shan-->Sheung Tung Au-->Sunset Peak-->Pak Kung Au', '3.5 hr	', 'https://1.bp.blogspot.com/-VW7xmcLbhmQ/YA1621JCvrI/AAAAAAAADsA/AsA7dD7_RnwzFF16SAsctb6SpZ6n1IiNwCLcBGAsYHQ/w640-h480/02%25E5%258D%2597%25E5%25B1%25B1.jpg');
INSERT INTO "public"."lantau" ("rid", "route", "time", "url") VALUES (3, 'Pak Kung Au-->Lantau Peak-->Ngong Ping', '4 hr	', 'https://1.bp.blogspot.com/-m8gDSLnOwYU/YA162sQqWRI/AAAAAAAADr8/KxcgF9SQ8k41Qac1IV8FhpVYOGA-e5TEwCLcBGAsYHQ/w640-h332/03%25E5%25A4%25A7%25E6%259D%25B1%25E5%25B1%25B1.jpg');
INSERT INTO "public"."lantau" ("rid", "route", "time", "url") VALUES (4, 'Ngong Ping-->Shum Wat Road', '1.5 hr', 'https://1.bp.blogspot.com/-ZjWKh4cv4_w/YA1639iVD7I/AAAAAAAADsM/vUUWhR4TJ8gCkE4OtehLWqOC376qFmhLwCLcBGAsYHQ/w640-h308/05%25E5%25AF%25B6%25E8%2593%25AE%25E5%25AF%25BA.jpg');
INSERT INTO "public"."lantau" ("rid", "route", "time", "url") VALUES (5, 'Shum Wat Road-->Kwun Yam Shan-->Keung Shan-->Ling Wui Shan-->Man Cheung Po-->LUNG TSAI NG YUEN', '3.5 hr	', 'https://1.bp.blogspot.com/-yFYzmf-NDCM/YA164iTBV6I/AAAAAAAADsQ/TSbwqY-ubaMqzMV-tRvGS7OOUxsaKlWAQCLcBGAsYHQ/w640-h462/06%25E6%2582%259F%25E5%259C%2592.jpg');
COMMIT;

-- ----------------------------
-- Primary Key structure for table lantau
-- ----------------------------
ALTER TABLE "public"."lantau" ADD CONSTRAINT "lantau_pkey" PRIMARY KEY ("rid");
