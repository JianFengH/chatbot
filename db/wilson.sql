-- ----------------------------
-- Table structure for wilson
-- ----------------------------
DROP TABLE IF EXISTS "public"."wilson";
CREATE TABLE "public"."wilson" (
  "rid" int8 NOT NULL,
  "route" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "time" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "url" varchar(255) COLLATE "pg_catalog"."default"
)
;
ALTER TABLE "public"."wilson" OWNER TO "postgres";

-- ----------------------------
-- Records of wilson
-- ----------------------------
BEGIN;
INSERT INTO "public"."wilson" ("rid", "route", "time", "url") VALUES (1, 'Stanley Gap Road-->THE TWINS-->Tsin Shui Wan Au-->VIOLET HILL-->Hong Kong Parkview', '2.5 hr', 'http://hike.bmgdemo.com/uploads/images/4trail/wt/IMG_2656_mod.jpg');
INSERT INTO "public"."wilson" ("rid", "route", "time", "url") VALUES (2, 'Hong Kong Parkview-->Jardine''s Lookout-->Siu Ma Shan-->Mount Parker Road-->Kornhill', '2 hr', 'http://hike.bmgdemo.com/uploads/images/4trail/hkt/IMG_1699.JPG');
INSERT INTO "public"."wilson" ("rid", "route", "time", "url") VALUES (3, 'Lam Tin-->Lei Yue Mun Road-->Ko Chiu Road-->O King Road-->Black Hill-->Ma Yau Tong-->Sam Long-->Tseng Lan Shue', '3 hr', 'http://hike.bmgdemo.com/uploads/images/4trail/wt/IMG_0399.jpg');
INSERT INTO "public"."wilson" ("rid", "route", "time", "url") VALUES (4, 'Tseng Lan Shue-->Wong Keng Zai-->Big Blue Lake-->Fei Ngo Shan Road-->Shatin Pass Road-->Sha Tin Pass', '3 hr', 'http://hike.bmgdemo.com/uploads/images/4trail/wt/IMG_7791.JPG');
INSERT INTO "public"."wilson" ("rid", "route", "time", "url") VALUES (5, 'Sha Tin Pass-->Amah Rock-->Kowloon Reservoir', '2.5 hr	', 'http://hike.bmgdemo.com/uploads/images/4trail/mt/IMG_6340_mod.jpg');
COMMIT;

-- ----------------------------
-- Primary Key structure for table wilson
-- ----------------------------
ALTER TABLE "public"."wilson" ADD CONSTRAINT "wilson_pkey" PRIMARY KEY ("rid");
