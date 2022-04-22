-- ----------------------------
-- Table structure for cookingvideo
-- ----------------------------
DROP TABLE IF EXISTS "public"."cookingvideo";
CREATE TABLE "public"."cookingvideo" (
  "cid" int8 NOT NULL,
  "image" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "url" varchar(255) COLLATE "pg_catalog"."default" NOT NULL
)
;
ALTER TABLE "public"."cookingvideo" OWNER TO "postgres";

-- ----------------------------
-- Records of cookingvideo
-- ----------------------------
BEGIN;
INSERT INTO "public"."cookingvideo" ("cid", "image", "url") VALUES (1, '1', 'https://www.youtube.com/watch?v=2ZxMNXBwHfQ&t=3s');
INSERT INTO "public"."cookingvideo" ("cid", "image", "url") VALUES (2, '2', 'https://www.youtube.com/watch?v=4YgOPaR9wUs&t=1s');
INSERT INTO "public"."cookingvideo" ("cid", "image", "url") VALUES (3, '3', 'https://www.youtube.com/watch?v=bC7W_wPtFvI&t=1s');
INSERT INTO "public"."cookingvideo" ("cid", "image", "url") VALUES (4, '4', 'https://www.youtube.com/watch?v=LB9KDxAOMvI&t=2s');
INSERT INTO "public"."cookingvideo" ("cid", "image", "url") VALUES (5, '5', 'https://www.youtube.com/watch?v=a-2n_g4AdDM&t=1s');
INSERT INTO "public"."cookingvideo" ("cid", "image", "url") VALUES (6, '6', 'https://www.youtube.com/watch?v=byJuxZ-H1-w&t=2s');
INSERT INTO "public"."cookingvideo" ("cid", "image", "url") VALUES (7, '7', 'https://www.youtube.com/watch?v=v4k4T9JzEZo&t=1s');
INSERT INTO "public"."cookingvideo" ("cid", "image", "url") VALUES (8, '8', 'https://www.youtube.com/watch?v=v4k4T9JzEZo&t=1s');
INSERT INTO "public"."cookingvideo" ("cid", "image", "url") VALUES (9, '9', 'https://www.youtube.com/watch?v=9xppRtAUJQk&t=1s');
INSERT INTO "public"."cookingvideo" ("cid", "image", "url") VALUES (10, '10', 'https://www.youtube.com/watch?v=ci_1T4tuJSo&t=1s');
COMMIT;

-- ----------------------------
-- Primary Key structure for table cookingvideo
-- ----------------------------
ALTER TABLE "public"."cookingvideo" ADD CONSTRAINT "cookingvideo_pkey" PRIMARY KEY ("cid");
