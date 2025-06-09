--
-- PostgreSQL database dump
--

-- Dumped from database version 17.5
-- Dumped by pg_dump version 17.5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: ERP_gym_class; Type: TABLE DATA; Schema: public; Owner: harrison
--

INSERT INTO public."ERP_gym_class" (id, title, description, archive, max_participants) VALUES (1, 'CrossFit', 'This Class Focuses on Fast Paced Movement', false, '14');
INSERT INTO public."ERP_gym_class" (id, title, description, archive, max_participants) VALUES (2, 'Boxing', 'Boxing Class', false, '10');
INSERT INTO public."ERP_gym_class" (id, title, description, archive, max_participants) VALUES (3, 'Teen Crossfit', 'Crossfit class for Teens', false, NULL);
INSERT INTO public."ERP_gym_class" (id, title, description, archive, max_participants) VALUES (4, 'Strength and Conditioning', 'Weight Lifting and Stuff', false, NULL);
INSERT INTO public."ERP_gym_class" (id, title, description, archive, max_participants) VALUES (5, 'Swimming', 'Laps My dude', false, NULL);
INSERT INTO public."ERP_gym_class" (id, title, description, archive, max_participants) VALUES (6, 'HIIT', 'Hight Intensity Interval Traning', false, NULL);
INSERT INTO public."ERP_gym_class" (id, title, description, archive, max_participants) VALUES (7, 'Pilates', 'Pilates class for good stretching.', false, NULL);
INSERT INTO public."ERP_gym_class" (id, title, description, archive, max_participants) VALUES (8, 'Spin Class', 'This class is a bike riding class', false, NULL);
INSERT INTO public."ERP_gym_class" (id, title, description, archive, max_participants) VALUES (10, 'Yoga', 'Yoga Class with Ms BOON', false, NULL);
INSERT INTO public."ERP_gym_class" (id, title, description, archive, max_participants) VALUES (13, 'Free Weights Time', 'Free Time for People in the Gym to workout and Train. Please come see staff i you require assistance.', false, NULL);


--
-- Data for Name: ERP_timetable_class_instance; Type: TABLE DATA; Schema: public; Owner: harrison
--

INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (1, '05:00', 'a', 8, 'Monday', '0');
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (2, '06:00', 'c', 2, 'Monday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (3, '07:00', 'a', 2, 'Monday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (4, '08:00', 'a', 2, 'Monday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (5, '09:00', 'a', 6, 'Monday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (6, '10:00', 'a', 2, 'Monday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (7, '11:00', 'a', 2, 'Monday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (8, '12:00', 'a', 4, 'Monday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (9, '13:00', 'a', 2, 'Monday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (10, '14:00', 'a', 2, 'Monday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (11, '15:00', 'a', 2, 'Monday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (12, '16:00', 'a', 2, 'Monday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (13, '17:00', 'a', 2, 'Monday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (14, '18:00', 'a', 2, 'Monday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (15, '07:00', 'a', 1, 'Tuesday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (16, '08:00', 'a', 1, 'Tuesday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (17, '09:00', 'a', 4, 'Tuesday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (18, '10:00', 'a', 8, 'Tuesday', '1');
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (19, '11:00', 'a', 13, 'Tuesday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (20, '12:00', 'a', 1, 'Tuesday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (21, '13:00', 'a', 1, 'Tuesday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (22, '14:00', 'a', 1, 'Tuesday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (23, '15:00', 'a', 6, 'Tuesday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (24, '16:00', 'a', 1, 'Tuesday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (25, '17:00', 'a', 1, 'Tuesday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (26, '05:00', 'a', 3, 'Tuesday', '2');
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (27, '06:00', 'a', 1, 'Tuesday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (28, '18:00', 'a', 1, 'Tuesday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (29, '05:00', 'a', 5, 'Wednesday', '2');
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (30, '05:00', 'a', 4, 'Thursday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (31, '05:00', 'a', 4, 'Friday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (32, '05:00', 'a', 10, 'Saturday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (33, '05:00', 'a', 3, 'Sunday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (34, '06:00', 'a', 1, 'Wednesday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (35, '06:00', 'a', 7, 'Thursday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (36, '06:00', 'a', 6, 'Friday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (37, '06:00', 'a', 5, 'Saturday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (38, '06:00', 'a', 3, 'Sunday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (39, '07:00', 'a', 6, 'Wednesday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (41, '07:00', 'a', 3, 'Friday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (42, '07:00', 'a', 5, 'Saturday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (43, '07:00', 'a', 3, 'Sunday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (44, '08:00', 'a', 6, 'Wednesday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (45, '07:00', 'a', 7, 'Thursday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (46, '08:00', 'a', 7, 'Thursday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (47, '08:00', 'a', 7, 'Friday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (48, '08:00', 'a', 5, 'Saturday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (49, '08:00', 'a', 3, 'Sunday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (50, '09:00', 'a', 4, 'Wednesday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (51, '09:00', 'a', 7, 'Thursday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (52, '09:00', 'a', 6, 'Friday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (53, '09:00', 'a', 5, 'Saturday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (54, '09:00', 'a', 3, 'Sunday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (55, '10:00', 'a', 6, 'Wednesday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (56, '10:00', 'c', 7, 'Thursday', '2');
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (57, '10:00', 'a', 5, 'Friday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (58, '10:00', 'a', 5, 'Saturday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (59, '10:00', 'a', 3, 'Sunday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (60, '11:00', 'a', 6, 'Sunday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (61, '12:00', 'a', 4, 'Wednesday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (62, '12:00', 'a', 7, 'Thursday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (63, '12:00', 'a', 2, 'Friday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (64, '12:00', 'a', 3, 'Saturday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (65, '12:00', 'a', 3, 'Sunday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (66, '13:00', 'a', 6, 'Wednesday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (67, '13:00', 'a', 7, 'Thursday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (68, '13:00', 'a', 1, 'Friday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (69, '13:00', 'a', 5, 'Saturday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (70, '13:00', 'a', NULL, 'Sunday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (71, '14:00', 'a', 8, 'Wednesday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (72, '14:00', 'a', 7, 'Thursday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (73, '14:00', 'a', 3, 'Friday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (74, '14:00', 'a', 5, 'Saturday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (75, '14:00', 'a', NULL, 'Sunday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (76, '15:00', 'a', 6, 'Wednesday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (77, '15:00', 'a', 7, 'Thursday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (78, '15:00', 'a', 8, 'Friday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (79, '15:00', 'a', NULL, 'Saturday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (80, '15:00', 'a', NULL, 'Sunday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (81, '16:00', 'a', 6, 'Wednesday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (82, '16:00', 'a', 7, 'Thursday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (83, '16:00', 'a', 5, 'Friday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (84, '16:00', 'a', NULL, 'Saturday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (85, '16:00', 'a', NULL, 'Sunday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (86, '17:00', 'a', 6, 'Wednesday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (87, '17:00', 'a', 7, 'Thursday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (88, '17:00', 'a', 3, 'Friday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (89, '17:00', 'a', NULL, 'Saturday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (90, '17:00', 'a', NULL, 'Sunday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (91, '18:00', 'a', 6, 'Wednesday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (92, '18:00', 'a', 7, 'Thursday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (93, '18:00', 'a', 1, 'Friday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (94, '18:00', 'a', NULL, 'Saturday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (95, '18:00', 'a', NULL, 'Sunday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (96, '11:00', 'a', 6, 'Wednesday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (97, '11:00', 'a', 1, 'Thursday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (98, '11:00', 'a', 3, 'Friday', NULL);
INSERT INTO public."ERP_timetable_class_instance" (id, time_slot, status, gym_class_id, day, current_participants) VALUES (99, '11:00', 'a', 5, 'Saturday', NULL);


--
-- Data for Name: ERP_timetable; Type: TABLE DATA; Schema: public; Owner: harrison
--

INSERT INTO public."ERP_timetable" (id, title, mon5_id, mon6_id, mon10_id, mon11_id, mon12_id, mon13_id, mon14_id, mon15_id, mon16_id, mon17_id, mon18_id, mon7_id, mon8_id, mon9_id, tue10_id, tue11_id, tue12_id, tue13_id, tue14_id, tue15_id, tue16_id, tue17_id, tue18_id, tue5_id, tue6_id, tue7_id, tue8_id, tue9_id, fri10_id, fri11_id, fri12_id, fri13_id, fri14_id, fri15_id, fri16_id, fri17_id, fri18_id, fri5_id, fri6_id, fri7_id, fri8_id, fri9_id, sat10_id, sat11_id, sat12_id, sat13_id, sat14_id, sat15_id, sat16_id, sat17_id, sat18_id, sat5_id, sat6_id, sat7_id, sat8_id, sat9_id, sun10_id, sun11_id, sun12_id, sun13_id, sun14_id, sun15_id, sun16_id, sun17_id, sun18_id, sun5_id, sun6_id, sun7_id, sun8_id, sun9_id, thur10_id, thur11_id, thur12_id, thur13_id, thur14_id, thur15_id, thur16_id, thur17_id, thur18_id, thur5_id, thur6_id, thur7_id, thur8_id, thur9_id, wed10_id, wed11_id, wed12_id, wed13_id, wed14_id, wed15_id, wed16_id, wed17_id, wed18_id, wed5_id, wed6_id, wed7_id, wed8_id, wed9_id) VALUES (1, 'Normal Timetable', 1, 2, 6, 7, 8, 9, 10, 11, 12, 13, 14, 3, 4, 5, 18, 19, 20, 21, 22, 23, 24, 25, 28, 26, 27, 15, 16, 17, 57, 98, 63, 68, 73, 78, 83, 88, 93, 31, 36, 41, 47, 52, 58, 99, 64, 69, 74, 79, 84, 89, 94, 32, 37, 42, 48, 53, 59, 60, 65, 70, 75, 80, 85, 90, 95, 33, 38, 43, 49, 54, 56, 97, 62, 67, 72, 77, 82, 87, 92, 30, 35, 45, 46, 51, 55, 96, 61, 66, 71, 76, 81, 86, 91, 29, 34, 39, 44, 50);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: harrison
--

INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (3, 'pbkdf2_sha256$600000$yWm8ROdnlzDWn2mHxGHGkP$XmMCl3Vrvh1V9xJDh3ZmFiBf5G6FaHRh0L4NFgPMieY=', '2023-10-23 15:10:07.866+10', false, 'Gym_Member_1', '', '', '', false, true, '2023-10-20 15:02:09+10');
INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (2, 'pbkdf2_sha256$600000$8JMpBF48Bk2YgOt2TaOMSP$VgRWqqucsjxd1NIDOIboVTCY9AIlDn5//mOToK3dL10=', '2025-06-04 08:32:33.45994+10', true, 'ERPAdmin', '', '', 'plume521@outlook.com', true, true, '2023-10-20 14:49:13.644+10');


--
-- Data for Name: ERP_userprofile; Type: TABLE DATA; Schema: public; Owner: harrison
--

INSERT INTO public."ERP_userprofile" (id, bio, profile_picture, user_id, is_staff, date_of_birth, first_name, gender, last_name, email, mobile, post_code, postal_address, prefered_traning_id, is_paid, last_payment, next_payment) VALUES (2, '', 'profile_pics/Gym_Member_1.jpg', 3, false, '1998-06-26', 'Kara', 'F', 'Daymon', 'karadaymon@yahoo.com.au', 415047883, 4074, '3 Langlo st Riverhills', 10, false, '2025-04-15 09:00:00+10', '2025-04-15 14:15:00+10');
INSERT INTO public."ERP_userprofile" (id, bio, profile_picture, user_id, is_staff, date_of_birth, first_name, gender, last_name, email, mobile, post_code, postal_address, prefered_traning_id, is_paid, last_payment, next_payment) VALUES (1, '', 'profile_pics/ERPAdmin.jpg', 2, true, '1998-02-26', 'Harrison', 'M', 'Plume', 'plume521@outlook.com', 434364053, 4074, '3 Langlo St', 13, false, '2025-04-15 09:00:00+10', '2025-04-15 14:36:00+10');


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: harrison
--

INSERT INTO public.auth_group (id, name) VALUES (1, 'Gym Staff Members');


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: harrison
--

INSERT INTO public.django_content_type (id, app_label, model) VALUES (1, 'admin', 'logentry');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (2, 'auth', 'permission');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (3, 'auth', 'group');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (4, 'auth', 'user');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (6, 'sessions', 'session');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (7, 'ERP', 'gym_class');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (8, 'ERP', 'timetable_class_instance');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (9, 'ERP', 'timetable');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (10, 'ERP', 'userprofile');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (11, 'django_q', 'schedule');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (12, 'django_q', 'task');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (13, 'django_q', 'failure');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (14, 'django_q', 'success');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (15, 'django_q', 'ormq');


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: harrison
--

INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (13, 'Can add user', 4, 'add_user');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (14, 'Can change user', 4, 'change_user');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (15, 'Can delete user', 4, 'delete_user');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (16, 'Can view user', 4, 'view_user');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (21, 'Can add session', 6, 'add_session');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (22, 'Can change session', 6, 'change_session');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (23, 'Can delete session', 6, 'delete_session');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (24, 'Can view session', 6, 'view_session');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (25, 'Can add gym_class', 7, 'add_gym_class');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (26, 'Can change gym_class', 7, 'change_gym_class');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (27, 'Can delete gym_class', 7, 'delete_gym_class');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (28, 'Can view gym_class', 7, 'view_gym_class');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (29, 'Can add timetable_class_instance', 8, 'add_timetable_class_instance');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (30, 'Can change timetable_class_instance', 8, 'change_timetable_class_instance');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (31, 'Can delete timetable_class_instance', 8, 'delete_timetable_class_instance');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (32, 'Can view timetable_class_instance', 8, 'view_timetable_class_instance');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (33, 'Can add timetable', 9, 'add_timetable');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (34, 'Can change timetable', 9, 'change_timetable');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (35, 'Can delete timetable', 9, 'delete_timetable');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (36, 'Can view timetable', 9, 'view_timetable');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (37, 'Can update the Timetable', 9, 'update_timetable');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (38, 'Can add user profile', 10, 'add_userprofile');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (39, 'Can change user profile', 10, 'change_userprofile');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (40, 'Can delete user profile', 10, 'delete_userprofile');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (41, 'Can view user profile', 10, 'view_userprofile');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (42, 'Can add Scheduled task', 11, 'add_schedule');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (43, 'Can change Scheduled task', 11, 'change_schedule');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (44, 'Can delete Scheduled task', 11, 'delete_schedule');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (45, 'Can view Scheduled task', 11, 'view_schedule');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (46, 'Can add task', 12, 'add_task');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (47, 'Can change task', 12, 'change_task');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (48, 'Can delete task', 12, 'delete_task');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (49, 'Can view task', 12, 'view_task');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (50, 'Can add Failed task', 13, 'add_failure');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (51, 'Can change Failed task', 13, 'change_failure');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (52, 'Can delete Failed task', 13, 'delete_failure');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (53, 'Can view Failed task', 13, 'view_failure');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (54, 'Can add Successful task', 14, 'add_success');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (55, 'Can change Successful task', 14, 'change_success');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (56, 'Can delete Successful task', 14, 'delete_success');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (57, 'Can view Successful task', 14, 'view_success');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (58, 'Can add Queued task', 15, 'add_ormq');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (59, 'Can change Queued task', 15, 'change_ormq');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (60, 'Can delete Queued task', 15, 'delete_ormq');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (61, 'Can view Queued task', 15, 'view_ormq');


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: harrison
--



--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: harrison
--



--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: harrison
--



--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: harrison
--



--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: harrison
--

INSERT INTO public.django_migrations (id, app, name, applied) VALUES (1, 'contenttypes', '0001_initial', '2025-06-04 08:26:01.646192+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (2, 'auth', '0001_initial', '2025-06-04 08:26:01.677445+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (3, 'ERP', '0001_initial', '2025-06-04 08:26:01.693071+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (4, 'ERP', '0002_timetable_class_instance_day', '2025-06-04 08:26:01.693071+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (5, 'ERP', '0003_alter_timetable_class_instance_day_and_more', '2025-06-04 08:26:01.708698+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (6, 'ERP', '0004_timetable', '2025-06-04 08:26:01.708698+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (7, 'ERP', '0005_timetable_mon6', '2025-06-04 08:26:01.708698+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (8, 'ERP', '0006_timetable_mon10_timetable_mon11_timetable_mon12_and_more', '2025-06-04 08:26:01.755597+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (9, 'ERP', '0007_alter_timetable_class_instance_gym_class', '2025-06-04 08:26:01.758422+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (10, 'ERP', '0008_timetable_tue10_timetable_tue11_timetable_tue12_and_more', '2025-06-04 08:26:01.788081+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (11, 'ERP', '0009_alter_timetable_class_instance_options', '2025-06-04 08:26:01.803708+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (12, 'ERP', '0010_timetable_fri10_timetable_fri11_timetable_fri12_and_more', '2025-06-04 08:26:02.163109+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (13, 'ERP', '0011_alter_timetable_mon10_alter_timetable_mon11_and_more', '2025-06-04 08:26:02.23087+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (14, 'ERP', '0012_alter_timetable_mon10_alter_timetable_mon11_and_more', '2025-06-04 08:26:02.30318+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (15, 'ERP', '0013_timetable_class_instance_current_participants_and_more', '2025-06-04 08:26:02.318806+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (16, 'ERP', '0014_timetable_class_instance_xd', '2025-06-04 08:26:02.318806+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (17, 'ERP', '0015_remove_timetable_class_instance_xd', '2025-06-04 08:26:02.334432+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (18, 'ERP', '0016_userprofile', '2025-06-04 08:26:02.334432+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (19, 'ERP', '0017_alter_userprofile_options', '2025-06-04 08:26:02.334432+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (20, 'ERP', '0018_userprofile_is_staff', '2025-06-04 08:26:02.350058+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (21, 'ERP', '0019_alter_userprofile_profile_picture', '2025-06-04 08:26:02.350058+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (22, 'ERP', '0020_alter_userprofile_is_staff', '2025-06-04 08:26:02.350058+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (23, 'ERP', '0021_alter_timetable_options', '2025-06-04 08:26:02.365684+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (24, 'ERP', '0022_alter_userprofile_is_staff', '2025-06-04 08:26:02.365684+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (25, 'ERP', '0023_alter_userprofile_profile_picture', '2025-06-04 08:26:02.365684+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (26, 'ERP', '0024_alter_userprofile_profile_picture', '2025-06-04 08:26:02.381311+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (27, 'ERP', '0025_gym_class_max_participants', '2025-06-04 08:26:02.381311+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (28, 'ERP', '0026_remove_timetable_class_instance_max_participants', '2025-06-04 08:26:02.381311+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (29, 'ERP', '0027_alter_timetable_class_instance_options', '2025-06-04 08:26:02.396937+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (30, 'ERP', '0028_alter_timetable_class_instance_options', '2025-06-04 08:26:02.396937+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (31, 'ERP', '0029_userprofile_date_of_birth_userprofile_first_name_and_more', '2025-06-04 08:26:02.412563+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (32, 'ERP', '0030_userprofile_email_userprofile_mobile_and_more', '2025-06-04 08:26:02.428189+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (33, 'ERP', '0031_userprofile_is_paid_userprofile_last_payment_and_more', '2025-06-04 08:26:02.443816+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (34, 'admin', '0001_initial', '2025-06-04 08:26:02.459442+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (35, 'admin', '0002_logentry_remove_auto_add', '2025-06-04 08:26:02.459442+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (36, 'admin', '0003_logentry_add_action_flag_choices', '2025-06-04 08:26:02.475068+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (37, 'contenttypes', '0002_remove_content_type_name', '2025-06-04 08:26:02.475068+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (38, 'auth', '0002_alter_permission_name_max_length', '2025-06-04 08:26:02.490694+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (39, 'auth', '0003_alter_user_email_max_length', '2025-06-04 08:26:02.490694+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (40, 'auth', '0004_alter_user_username_opts', '2025-06-04 08:26:02.50632+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (41, 'auth', '0005_alter_user_last_login_null', '2025-06-04 08:26:02.50632+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (42, 'auth', '0006_require_contenttypes_0002', '2025-06-04 08:26:02.50632+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (43, 'auth', '0007_alter_validators_add_error_messages', '2025-06-04 08:26:02.521946+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (44, 'auth', '0008_alter_user_username_max_length', '2025-06-04 08:26:02.537573+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (45, 'auth', '0009_alter_user_last_name_max_length', '2025-06-04 08:26:02.537573+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (46, 'auth', '0010_alter_group_name_max_length', '2025-06-04 08:26:02.553199+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (47, 'auth', '0011_update_proxy_permissions', '2025-06-04 08:26:02.553199+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (48, 'auth', '0012_alter_user_first_name_max_length', '2025-06-04 08:26:02.568825+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (49, 'django_q', '0001_initial', '2025-06-04 08:26:02.568825+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (50, 'django_q', '0002_auto_20150630_1624', '2025-06-04 08:26:02.568825+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (51, 'django_q', '0003_auto_20150708_1326', '2025-06-04 08:26:02.584451+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (52, 'django_q', '0004_auto_20150710_1043', '2025-06-04 08:26:02.584451+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (53, 'django_q', '0005_auto_20150718_1506', '2025-06-04 08:26:02.584451+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (54, 'django_q', '0006_auto_20150805_1817', '2025-06-04 08:26:02.584451+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (55, 'django_q', '0007_ormq', '2025-06-04 08:26:02.600077+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (56, 'django_q', '0008_auto_20160224_1026', '2025-06-04 08:26:02.600077+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (57, 'django_q', '0009_auto_20171009_0915', '2025-06-04 08:26:02.600077+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (58, 'django_q', '0010_auto_20200610_0856', '2025-06-04 08:26:02.615703+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (59, 'django_q', '0011_auto_20200628_1055', '2025-06-04 08:26:02.615703+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (60, 'django_q', '0012_auto_20200702_1608', '2025-06-04 08:26:02.615703+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (61, 'django_q', '0013_task_attempt_count', '2025-06-04 08:26:02.615703+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (62, 'django_q', '0014_schedule_cluster', '2025-06-04 08:26:02.615703+10');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (63, 'sessions', '0001_initial', '2025-06-04 08:26:02.631329+10');


--
-- Data for Name: django_q_ormq; Type: TABLE DATA; Schema: public; Owner: harrison
--



--
-- Data for Name: django_q_schedule; Type: TABLE DATA; Schema: public; Owner: harrison
--



--
-- Data for Name: django_q_task; Type: TABLE DATA; Schema: public; Owner: harrison
--



--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: harrison
--

INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('uha8wezfm98clqvqse5csq6d6fcq4r3n', '.eJxVjEEOwiAQRe_C2pAphaG4dO8ZyDBDpWrapLQr492VpAvd_fz38l4q0r6VuNe8xknUWRl1-v0S8SPPDcid5tuieZm3dUq6KfqgVV8Xyc_L4f4FCtXSskIWPWUrwKM3OHohDA4cBkx9FwbAjO47rOmN4w765IUhAYDlMLB6fwDMjTba:1uMaBN:uIR8Zzb-jTc4Skz0ImGqmn9FS2qYDPLACaBDelIiQrU', '2025-06-18 08:32:33.462817+10');


--
-- Name: ERP_gym_class_id_seq; Type: SEQUENCE SET; Schema: public; Owner: harrison
--

SELECT pg_catalog.setval('public."ERP_gym_class_id_seq"', 13, true);


--
-- Name: ERP_timetable_class_instance_id_seq; Type: SEQUENCE SET; Schema: public; Owner: harrison
--

SELECT pg_catalog.setval('public."ERP_timetable_class_instance_id_seq"', 99, true);


--
-- Name: ERP_timetable_id_seq; Type: SEQUENCE SET; Schema: public; Owner: harrison
--

SELECT pg_catalog.setval('public."ERP_timetable_id_seq"', 1, true);


--
-- Name: ERP_userprofile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: harrison
--

SELECT pg_catalog.setval('public."ERP_userprofile_id_seq"', 2, true);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: harrison
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, true);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: harrison
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: harrison
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 61, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: harrison
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: harrison
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 3, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: harrison
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: harrison
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: harrison
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 15, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: harrison
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 63, true);


--
-- Name: django_q_ormq_id_seq; Type: SEQUENCE SET; Schema: public; Owner: harrison
--

SELECT pg_catalog.setval('public.django_q_ormq_id_seq', 1, false);


--
-- Name: django_q_schedule_id_seq; Type: SEQUENCE SET; Schema: public; Owner: harrison
--

SELECT pg_catalog.setval('public.django_q_schedule_id_seq', 1, false);


--
-- PostgreSQL database dump complete
--

