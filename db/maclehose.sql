-- ----------------------------
-- Table structure for maclehose
-- ----------------------------
DROP TABLE IF EXISTS "public"."maclehose";
CREATE TABLE "public"."maclehose" (
  "rid" int8 NOT NULL,
  "route" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "time" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "url" varchar(255) COLLATE "pg_catalog"."default"
)
;
ALTER TABLE "public"."maclehose" OWNER TO "postgres";

-- ----------------------------
-- Records of maclehose
-- ----------------------------
BEGIN;
INSERT INTO "public"."maclehose" ("rid", "route", "time", "url") VALUES (2, '
LONG KE-->Sai Wan Shan-->Chui Tung Au-->SAI WAN-->Ham Tin Wan-->Tai Long Au-->CHEK KENG-->Pak Tam Au', '4.5 hr', 'https://cdn.reubird.hk/large%2Fblogs%2Fmaclehose-trail-hiking%2FM2.jpg');
INSERT INTO "public"."maclehose" ("rid", "route", "time", "url") VALUES (1, 'Pak Tam Road-->Man Yee Au-->High Island (West Dam)-->High Island (East Dam)-->LONG KE', '3.5 hr	', 'https://cdn.reubird.hk/large%2Fblogs%2Fmaclehose-trail-hiking%2FM1.jpg');
INSERT INTO "public"."maclehose" ("rid", "route", "time", "url") VALUES (3, 'Pak Tam Au-->NGAU YEE SHEK SHAN-->CHEUNG SHEUNG-->WA MEI SHAN-->KAI KUNG SHAN-->Shui Long Wo', '3.5 hr	', 'https://cdn.reubird.hk/large%2Fblogs%2Fmaclehose-trail-hiking%2FM3.jpg');
INSERT INTO "public"."maclehose" ("rid", "route", "time", "url") VALUES (4, 'Shui Long Wo-->Ma On Shan-->Ngong Ping-->Mau Ping-->West Buffalo Hill-->Tate''s Cairn', '5 hr', 'https://cdn.reubird.hk/large%2Fblogs%2Fmaclehose-trail-hiking%2FM4.jpg');
INSERT INTO "public"."maclehose" ("rid", "route", "time", "url") VALUES (5, 'Tate''s Cairn-->Sha Tin Pass-->Lion Rock-->Beacon Hill-->Tai Po Road', '3.5 hr	', 'https://cdn.reubird.hk/large%2Fblogs%2Fmaclehose-trail-hiking%2FM5.jpg');
COMMIT;

-- ----------------------------
-- Primary Key structure for table maclehose
-- ----------------------------
ALTER TABLE "public"."maclehose" ADD CONSTRAINT "testtable_pkey" PRIMARY KEY ("rid");
