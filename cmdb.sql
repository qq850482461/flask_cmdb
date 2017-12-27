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
-- Table structure for table `email`
--

DROP TABLE IF EXISTS `email`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `email` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(80) DEFAULT NULL,
  `password` varchar(80) DEFAULT NULL,
  `description` varchar(80) DEFAULT NULL,
  `created_time` datetime DEFAULT NULL,
  `emailserver_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `emailserver_id` (`emailserver_id`),
  CONSTRAINT `email_ibfk_1` FOREIGN KEY (`emailserver_id`) REFERENCES `email_server` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `email`
--

LOCK TABLES `email` WRITE;
/*!40000 ALTER TABLE `email` DISABLE KEYS */;
/*!40000 ALTER TABLE `email` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `email_server`
--

DROP TABLE IF EXISTS `email_server`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `email_server` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) DEFAULT NULL,
  `pop` varchar(80) DEFAULT NULL,
  `pop_port` int(11) DEFAULT NULL,
  `smtp` varchar(80) DEFAULT NULL,
  `smtp_port` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `email_server`
--

LOCK TABLES `email_server` WRITE;
/*!40000 ALTER TABLE `email_server` DISABLE KEYS */;
/*!40000 ALTER TABLE `email_server` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `email_supplier`
--

DROP TABLE IF EXISTS `email_supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `email_supplier` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(80) DEFAULT NULL,
  `web` varchar(80) DEFAULT NULL,
  `operator` varchar(80) DEFAULT NULL,
  `username` varchar(80) DEFAULT NULL,
  `password` varchar(80) DEFAULT NULL,
  `created_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `email_supplier`
--

LOCK TABLES `email_supplier` WRITE;
/*!40000 ALTER TABLE `email_supplier` DISABLE KEYS */;
/*!40000 ALTER TABLE `email_supplier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ip_address`
--

DROP TABLE IF EXISTS `ip_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ip_address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(80) DEFAULT NULL,
  `mac` varchar(80) DEFAULT NULL,
  `hostname` varchar(80) DEFAULT NULL,
  `enable` tinyint(1) DEFAULT NULL,
  `created_time` datetime DEFAULT NULL,
  `ip_category` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ip_category` (`ip_category`),
  CONSTRAINT `ip_address_ibfk_1` FOREIGN KEY (`ip_category`) REFERENCES `ip_category` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ip_address`
--

LOCK TABLES `ip_address` WRITE;
/*!40000 ALTER TABLE `ip_address` DISABLE KEYS */;
/*!40000 ALTER TABLE `ip_address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ip_category`
--

DROP TABLE IF EXISTS `ip_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ip_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) DEFAULT NULL,
  `created_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ip_category`
--

LOCK TABLES `ip_category` WRITE;
/*!40000 ALTER TABLE `ip_category` DISABLE KEYS */;
INSERT INTO `ip_category` VALUES (1,'唐朝','2017-09-25 15:38:23'),(2,'蜗蜗游','2017-09-25 15:38:48');
/*!40000 ALTER TABLE `ip_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `node`
--

DROP TABLE IF EXISTS `node`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `node` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(80) DEFAULT NULL,
  `label` varchar(80) DEFAULT NULL,
  `icon` varchar(80) DEFAULT NULL,
  `order` int(11) DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `node`
--

LOCK TABLES `node` WRITE;
/*!40000 ALTER TABLE `node` DISABLE KEYS */;
INSERT INTO `node` VALUES (2,'/email_server/','查询邮箱','',2,5),(3,'/email/','邮箱管理','fa-check',1,5),(4,'/email_support/','邮箱供应商','',3,5),(5,'#','邮箱管理','fa-angellist',2,0),(6,'#','资产管理','fa-circle-o',3,0),(7,'/ip_address','ip地址池','',1,6),(25,'/','主页','fa-car',1,0),(28,'#','个人中心','fa-android',4,0),(29,'/resetpw','修改密码','',1,28),(30,'/adduser','增加用户','',3,28),(31,'/menu','菜单管理','',4,28),(32,'/roles','角色管理','',2,28);
/*!40000 ALTER TABLE `node` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` VALUES (1,'admin','管理员');
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role_node`
--

DROP TABLE IF EXISTS `role_node`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `role_node` (
  `role_id` int(11) DEFAULT NULL,
  `node_id` int(11) DEFAULT NULL,
  KEY `node_id` (`node_id`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `role_node_ibfk_1` FOREIGN KEY (`node_id`) REFERENCES `node` (`id`),
  CONSTRAINT `role_node_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role_node`
--

LOCK TABLES `role_node` WRITE;
/*!40000 ALTER TABLE `role_node` DISABLE KEYS */;
INSERT INTO `role_node` VALUES (1,4),(1,32),(1,30),(1,31),(1,5),(1,3),(1,29),(1,6),(1,25),(1,28),(1,7),(1,2);
/*!40000 ALTER TABLE `role_node` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(80) NOT NULL,
  `password_hash` varchar(255) DEFAULT NULL,
  `created_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (5,'admin','pbkdf2:sha256:50000$jeslGXi4$ca012c7c022b9160d3ac514cf98a14c8560a2c3a6315856019170bec3ac4b0f4','2017-12-22 08:16:34');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_role`
--

DROP TABLE IF EXISTS `user_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_role` (
  `user_id` int(11) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL,
  KEY `role_id` (`role_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `user_role_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`),
  CONSTRAINT `user_role_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

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

-- Dump completed on 2017-12-27 14:06:03
