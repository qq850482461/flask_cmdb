-- MySQL dump 10.13  Distrib 5.6.34, for Win64 (x86_64)
--
-- Host: localhost    Database: cmdb
-- ------------------------------------------------------
-- Server version	5.6.34-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `email`
--

LOCK TABLES `email` WRITE;
/*!40000 ALTER TABLE `email` DISABLE KEYS */;
/*!40000 ALTER TABLE `email` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `email_server`
--

LOCK TABLES `email_server` WRITE;
/*!40000 ALTER TABLE `email_server` DISABLE KEYS */;
/*!40000 ALTER TABLE `email_server` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `email_supplier`
--

LOCK TABLES `email_supplier` WRITE;
/*!40000 ALTER TABLE `email_supplier` DISABLE KEYS */;
/*!40000 ALTER TABLE `email_supplier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `ip_address`
--

LOCK TABLES `ip_address` WRITE;
/*!40000 ALTER TABLE `ip_address` DISABLE KEYS */;
/*!40000 ALTER TABLE `ip_address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `ip_category`
--

LOCK TABLES `ip_category` WRITE;
/*!40000 ALTER TABLE `ip_category` DISABLE KEYS */;
INSERT INTO `ip_category` VALUES (1,'唐朝','2017-09-25 15:38:23'),(2,'蜗蜗游','2017-09-25 15:38:48');
/*!40000 ALTER TABLE `ip_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `node`
--

LOCK TABLES `node` WRITE;
/*!40000 ALTER TABLE `node` DISABLE KEYS */;
INSERT INTO `node` VALUES (2,'/email_server/','查询邮箱','',2,5),(3,'/email/','邮箱管理','fa-check',1,5),(4,'/email_support/','邮箱供应商','',3,5),(5,'#','邮箱管理','fa-angellist',2,0),(6,'#','资产管理','fa-circle-o',3,0),(7,'/ip_address','ip地址池','',1,6),(25,'/','主页','fa-car',1,0),(28,'#','个人中心','fa-android',4,0),(29,'/resetpw','修改密码','',1,28),(30,'/adduser','增加用户','',3,28),(31,'/menu','菜单管理','',4,28),(32,'/roles','角色管理','',2,28);
/*!40000 ALTER TABLE `node` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` VALUES (1,'admin','管理员');
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `role_node`
--

LOCK TABLES `role_node` WRITE;
/*!40000 ALTER TABLE `role_node` DISABLE KEYS */;
INSERT INTO `role_node` VALUES (1,4),(1,32),(1,30),(1,31),(1,5),(1,3),(1,29),(1,6),(1,25),(1,28),(1,7),(1,2);
/*!40000 ALTER TABLE `role_node` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (5,'admin','pbkdf2:sha256:50000$jeslGXi4$ca012c7c022b9160d3ac514cf98a14c8560a2c3a6315856019170bec3ac4b0f4','2017-12-22 08:16:34');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `user_role`
--

LOCK TABLES `user_role` WRITE;
/*!40000 ALTER TABLE `user_role` DISABLE KEYS */;
INSERT INTO `user_role` VALUES (5,1);
/*!40000 ALTER TABLE `user_role` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-12-22 16:51:56
