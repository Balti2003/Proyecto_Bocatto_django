-- MySQL dump 10.13  Distrib 8.0.43, for Linux (x86_64)
--
-- Host: localhost    Database: bocatto_db
-- ------------------------------------------------------
-- Server version	8.0.43-0ubuntu0.24.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (2,'Clientes'),(1,'Empleados');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add category',7,'add_category'),(26,'Can change category',7,'change_category'),(27,'Can delete category',7,'delete_category'),(28,'Can view category',7,'view_category'),(29,'Can add order',8,'add_order'),(30,'Can change order',8,'change_order'),(31,'Can delete order',8,'delete_order'),(32,'Can view order',8,'view_order'),(33,'Can add product',9,'add_product'),(34,'Can change product',9,'change_product'),(35,'Can delete product',9,'delete_product'),(36,'Can view product',9,'view_product'),(37,'Can add order item',10,'add_orderitem'),(38,'Can change order item',10,'change_orderitem'),(39,'Can delete order item',10,'delete_orderitem'),(40,'Can view order item',10,'view_orderitem');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$870000$72L7D0w2cDDoU3vUgnRpAO$X4z07ThktO2vs4kz6jpP3A0tV5WZn77YN/MdjtvBuX0=','2025-10-29 19:06:16.697022',1,'baltasar','Baltasar','Lomello','baltasarlomello@live.com',1,1,'2025-08-27 19:50:28.000000'),(2,'pbkdf2_sha256$870000$yhB79kaL7p9xwuec6NMep4$yiBg3GuO4N+IC7r1VigKxrUdV70fJcEKp+BQhEZIhSA=','2025-10-29 17:32:41.447046',0,'administrador','Admin','Bocatto','',1,1,'2025-09-23 16:57:04.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (3,1,2),(2,2,1);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2025-09-02 16:34:49.369399','1','Hamburguesas',1,'[{\"added\": {}}]',7,1),(2,'2025-09-02 16:37:09.766026','2','Pizzas',1,'[{\"added\": {}}]',7,1),(3,'2025-09-02 16:37:58.847553','2','Pizzas',2,'[]',7,1),(4,'2025-09-02 16:38:47.801640','3','Lomitos',1,'[{\"added\": {}}]',7,1),(5,'2025-09-02 16:42:16.910011','4','Sandwiches',1,'[{\"added\": {}}]',7,1),(6,'2025-09-02 16:47:02.986167','4','Sandwiches',2,'[{\"changed\": {\"fields\": [\"Descripcion\"]}}]',7,1),(7,'2025-09-02 16:47:45.477301','5','Papas',1,'[{\"added\": {}}]',7,1),(8,'2025-09-02 16:49:16.781595','6','Bebidas',1,'[{\"added\": {}}]',7,1),(9,'2025-09-02 16:51:44.647925','7','Postres',1,'[{\"added\": {}}]',7,1),(10,'2025-09-02 17:04:09.730541','1','Hamburguesas',2,'[]',7,1),(11,'2025-09-02 17:48:34.235891','1','Cheese',1,'[{\"added\": {}}]',9,1),(12,'2025-09-16 16:36:30.500883','1','baltasar',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\"]}}]',4,1),(13,'2025-09-16 17:27:00.574343','1','Empleados',1,'[{\"added\": {}}]',3,1),(14,'2025-09-16 17:27:06.256266','2','Clientes',1,'[{\"added\": {}}]',3,1),(15,'2025-09-16 17:59:35.919373','2','Cuarto de libra',1,'[{\"added\": {}}]',9,1),(16,'2025-09-16 18:00:44.885461','3','Bacon',1,'[{\"added\": {}}]',9,1),(17,'2025-09-16 18:01:48.421953','4','Clasica',1,'[{\"added\": {}}]',9,1),(18,'2025-09-16 18:03:29.325196','5','Tasty',1,'[{\"added\": {}}]',9,1),(19,'2025-09-16 18:04:08.632275','6','Mexa',1,'[{\"added\": {}}]',9,1),(20,'2025-09-16 18:28:58.486313','1','Pedido #1 - baltasar',3,'',8,1),(21,'2025-09-23 16:56:18.053804','1','baltasar',2,'[]',4,1),(22,'2025-09-23 16:57:05.486502','2','administrador',1,'[{\"added\": {}}]',4,1),(23,'2025-09-23 16:57:14.831801','2','administrador',2,'[]',4,1),(24,'2025-09-23 16:57:28.185085','2','administrador',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\"]}}]',4,1),(25,'2025-09-23 16:57:39.874255','2','administrador',2,'[{\"changed\": {\"fields\": [\"Staff status\"]}}]',4,1),(26,'2025-09-23 17:18:14.446195','2','administrador',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(27,'2025-09-23 17:18:27.348268','1','baltasar',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(28,'2025-09-30 16:38:53.111013','3','Pedido #3 - baltasar',2,'[{\"changed\": {\"fields\": [\"Estado\"]}}]',8,1),(29,'2025-09-30 16:57:48.343814','4','Pedido #4 - baltasar',2,'[{\"changed\": {\"fields\": [\"Estado\"]}}]',8,1),(30,'2025-10-01 19:44:10.278854','7','Chesse2',3,'',9,1),(31,'2025-10-01 20:38:36.194602','8','Pedido #8 - baltasar',3,'',8,1),(32,'2025-10-01 20:38:36.194643','7','Pedido #7 - baltasar',3,'',8,1),(33,'2025-10-01 20:38:36.194661','6','Pedido #6 - baltasar',3,'',8,1),(34,'2025-10-01 20:40:38.139640','10','Pedido #10 - baltasar',3,'',8,1),(35,'2025-10-01 20:40:38.139684','9','Pedido #9 - baltasar',3,'',8,1),(36,'2025-10-08 18:46:21.810326','11','Pedido #11 - baltasar',3,'',8,1),(37,'2025-10-08 19:04:19.016311','12','Pedido #12 - baltasar',3,'',8,1),(38,'2025-10-08 19:04:19.016370','5','Pedido #5 - baltasar',3,'',8,1),(39,'2025-10-08 19:04:19.016395','4','Pedido #4 - baltasar',3,'',8,1),(40,'2025-10-08 19:04:19.016415','3','Pedido #3 - baltasar',3,'',8,1),(41,'2025-10-08 19:04:19.016431','2','Pedido #2 - baltasar',3,'',8,1),(42,'2025-10-08 19:35:25.972827','15','Pedido #15 - baltasar',3,'',8,1),(43,'2025-10-08 20:17:00.263077','9','Cuatro Quesos',1,'[{\"added\": {}}]',9,1),(44,'2025-10-08 20:26:57.754525','10','Especial',1,'[{\"added\": {}}]',9,1),(45,'2025-10-08 20:31:35.154372','11','Brocoli',1,'[{\"added\": {}}]',9,1),(46,'2025-10-08 20:34:14.986188','12','Bacon',1,'[{\"added\": {}}]',9,1),(47,'2025-10-14 13:32:42.375007','8','Empanadas',1,'[{\"added\": {}}]',7,1),(48,'2025-10-14 13:33:41.261473','13','Empanadas de Carne',1,'[{\"added\": {}}]',9,1),(49,'2025-10-14 13:34:59.820025','14','Empanadas de JyQ',1,'[{\"added\": {}}]',9,1),(50,'2025-10-14 13:36:10.233934','15','Empanadas de Pollo',1,'[{\"added\": {}}]',9,1),(51,'2025-10-14 13:39:45.886246','14','Empanadas de JyQ',2,'[{\"changed\": {\"fields\": [\"Imagen\"]}}]',9,1),(52,'2025-10-14 13:41:29.842949','14','Empanadas de JyQ',3,'',9,1),(53,'2025-10-14 13:42:36.070122','16','Empanadas de JyQ',1,'[{\"added\": {}}]',9,1),(54,'2025-10-14 13:44:46.908534','13','Empanadas de Carne',2,'[{\"changed\": {\"fields\": [\"Imagen\"]}}]',9,1),(55,'2025-10-14 13:45:00.932460','15','Empanadas de Pollo',2,'[{\"changed\": {\"fields\": [\"Imagen\"]}}]',9,1),(56,'2025-10-14 13:46:00.928596','17','Empanadas Árabes',1,'[{\"added\": {}}]',9,1),(57,'2025-10-14 13:49:37.133668','18','Papas Fritas',1,'[{\"added\": {}}]',9,1),(58,'2025-10-14 13:50:50.508290','19','Papas Fritas con Cheddar y Bacon',1,'[{\"added\": {}}]',9,1),(59,'2025-10-14 13:52:05.546115','20','Papas Fritas con Huevo',1,'[{\"added\": {}}]',9,1),(60,'2025-10-14 13:52:34.627358','20','Papas Fritas con Huevo',2,'[{\"changed\": {\"fields\": [\"Categoria\"]}}]',9,1),(61,'2025-10-14 13:54:19.439961','3','Lomitos',3,'',7,1),(62,'2025-10-14 13:54:33.868496','4','Sandwiches',2,'[{\"changed\": {\"fields\": [\"Descripcion\"]}}]',7,1),(63,'2025-10-14 13:59:49.153739','21','Sandwich Milanesa',1,'[{\"added\": {}}]',9,1),(64,'2025-10-14 14:01:00.572949','22','Sandwich Lomito',1,'[{\"added\": {}}]',9,1),(65,'2025-10-14 14:05:23.969070','23','Coca-Cola',1,'[{\"added\": {}}]',9,1),(66,'2025-10-14 14:06:15.381047','24','Agua Mineral',1,'[{\"added\": {}}]',9,1),(67,'2025-10-14 14:09:27.987447','25','Agua Saborizada Manzana',1,'[{\"added\": {}}]',9,1),(68,'2025-10-14 14:10:32.735959','25','Agua Saborizada Manzana',2,'[{\"changed\": {\"fields\": [\"Descripcion\", \"Imagen\"]}}]',9,1),(69,'2025-10-14 14:10:40.377960','24','Agua Mineral',2,'[{\"changed\": {\"fields\": [\"Descripcion\"]}}]',9,1),(70,'2025-10-14 14:10:47.292265','23','Coca-Cola',2,'[{\"changed\": {\"fields\": [\"Descripcion\"]}}]',9,1),(71,'2025-10-14 14:11:58.277321','26','Agua Saborizada Pera',1,'[{\"added\": {}}]',9,1),(72,'2025-10-14 14:12:06.053311','26','Agua Saborizada Pera',2,'[{\"changed\": {\"fields\": [\"Precio\"]}}]',9,1),(73,'2025-10-14 14:17:37.129536','27','Postre Chocotorta',1,'[{\"added\": {}}]',9,1),(74,'2025-10-14 14:18:35.632627','28','Postre Oreo',1,'[{\"added\": {}}]',9,1),(75,'2025-10-28 17:06:53.110606','17','Pedido #17 - baltasar',2,'[{\"changed\": {\"fields\": [\"Estado\"]}}]',8,1),(76,'2025-10-29 19:17:04.323348','21','Pedido #21 - baltasar',3,'',8,1),(77,'2025-10-29 19:17:04.323390','20','Pedido #20 - baltasar',3,'',8,1),(78,'2025-10-29 19:24:29.801106','22','Pedido #22 - baltasar',3,'',8,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(7,'shop','category'),(8,'shop','order'),(10,'shop','orderitem'),(9,'shop','product');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-08-27 19:49:44.387926'),(2,'auth','0001_initial','2025-08-27 19:49:45.768677'),(3,'admin','0001_initial','2025-08-27 19:49:46.070064'),(4,'admin','0002_logentry_remove_auto_add','2025-08-27 19:49:46.082152'),(5,'admin','0003_logentry_add_action_flag_choices','2025-08-27 19:49:46.093942'),(6,'contenttypes','0002_remove_content_type_name','2025-08-27 19:49:46.289634'),(7,'auth','0002_alter_permission_name_max_length','2025-08-27 19:49:46.421471'),(8,'auth','0003_alter_user_email_max_length','2025-08-27 19:49:46.454697'),(9,'auth','0004_alter_user_username_opts','2025-08-27 19:49:46.463685'),(10,'auth','0005_alter_user_last_login_null','2025-08-27 19:49:46.577779'),(11,'auth','0006_require_contenttypes_0002','2025-08-27 19:49:46.583847'),(12,'auth','0007_alter_validators_add_error_messages','2025-08-27 19:49:46.599022'),(13,'auth','0008_alter_user_username_max_length','2025-08-27 19:49:46.741037'),(14,'auth','0009_alter_user_last_name_max_length','2025-08-27 19:49:46.878053'),(15,'auth','0010_alter_group_name_max_length','2025-08-27 19:49:46.909732'),(16,'auth','0011_update_proxy_permissions','2025-08-27 19:49:46.923638'),(17,'auth','0012_alter_user_first_name_max_length','2025-08-27 19:49:47.051136'),(18,'sessions','0001_initial','2025-08-27 19:49:47.140316'),(19,'shop','0001_initial','2025-08-27 19:49:47.827472'),(20,'shop','0002_remove_product_stock','2025-09-02 17:44:04.313582'),(21,'shop','0003_customuser','2025-09-16 17:52:28.061831'),(22,'shop','0004_delete_customuser','2025-09-16 17:52:28.182392'),(23,'shop','0005_order_metodo_entrega_order_metodo_pago','2025-10-01 20:23:28.402311'),(24,'shop','0006_alter_order_estado','2025-10-28 16:16:35.589013');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('upf5rhy5p3xq8n6f4kck87rw6zmn1647','.eJxVj8tuxCAMRf-F9YiQF0Nm2VU3_YbIBofQNhDxWI3y74VqFu3GlnyPj-UnW6HkfS2J4uoMe7Ce3f7OEPQX-RaYT_A2cB18jg55Q_grTfwjGPp-e7H_BDukvWmNmDSqeRhoAYn3ebsLhUrSsBkUZtRqlHqufUBcFqjcIo1aFG4b9WKaqlRDjC4H9niysRUfDoxU3fVu8L9AJhuigzp7hwNLtIUSpBqdkbSrq3ISgouG-uwM1L_6G3MHWPJ1qTvIOOjOGEzROaQOm5mf3rLrun4ApgVipQ:1vECfY:Ehmjy04iNQzgrUBOHTYVt_MzBaxrP7GatHr1sjAho5I','2025-11-12 20:21:20.781598');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shop_category`
--

DROP TABLE IF EXISTS `shop_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shop_category` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shop_category`
--

LOCK TABLES `shop_category` WRITE;
/*!40000 ALTER TABLE `shop_category` DISABLE KEYS */;
INSERT INTO `shop_category` VALUES (1,'Hamburguesas','Nuestras hamburguesas combinan carne de primera calidad con ingredientes frescos como lechuga, tomate, queso cheddar y salsas caseras. Ideales para quienes buscan un bocado rápido, contundente y lleno de sabor argentino.'),(2,'Pizzas','Nuestras pizzas al corte reflejan la tradición rioplatense: masa tierna y esponjosa, abundante mozzarella, salsa de tomate casera y una variedad de ingredientes clásicos como jamón, aceitunas, huevo, palmitos y más. Perfectas para compartir o disfrutar a solas.'),(4,'Sandwiches','Los clásicos de siempre en su mejor versión. Sándwiches sabrosos con variedad de panes e ingredientes, ideales para cualquier momento del día.'),(5,'Papas','El acompañamiento estrella de la comida rápida. Papas fritas crocantes en diferentes presentaciones: clásicas, con cheddar y bacon, provenzal o papas rústicas.'),(6,'Bebidas','La mejor variedad para refrescar tu pedido: agua mineral, gaseosas, aguas saborizadas, jugos y cervezas bien frías para completar la experiencia Bocatto.'),(7,'Postres','Un cierre perfecto para tu comida. Postres irresistibles como chocotorta, oreo, flan casero, helado de diferentes sabores, tiramisú y más.'),(8,'Empanadas','Ricas empanadas envueltas en masa que se rellenan con ingredientes salados o dulces, para luego ser cocidas al horno o frita.');
/*!40000 ALTER TABLE `shop_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shop_order`
--

DROP TABLE IF EXISTS `shop_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shop_order` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fecha` datetime(6) NOT NULL,
  `estado` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `total` decimal(10,2) NOT NULL,
  `usuario_id` int NOT NULL,
  `metodo_entrega` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `metodo_pago` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `shop_order_usuario_id_f38a01fb_fk_auth_user_id` (`usuario_id`),
  CONSTRAINT `shop_order_usuario_id_f38a01fb_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shop_order`
--

LOCK TABLES `shop_order` WRITE;
/*!40000 ALTER TABLE `shop_order` DISABLE KEYS */;
INSERT INTO `shop_order` VALUES (13,'2025-10-08 19:03:49.561853','cancelado',6400.00,1,'envio','efectivo'),(14,'2025-10-08 19:09:14.863706','pagado',18800.00,1,'retiro','efectivo'),(16,'2025-10-08 19:36:38.377757','enviado',32500.00,1,'delivery','transferencia'),(17,'2025-10-28 17:03:57.762023','pendiente_pago',11600.00,1,'delivery','transferencia'),(18,'2025-10-28 17:10:16.432723','pendiente_pago',12100.00,1,'retiro','transferencia'),(19,'2025-10-29 17:42:57.679414','pendiente_pago',32200.00,1,'retiro','transferencia'),(23,'2025-10-29 19:24:52.616512','pendiente_pago',8500.00,1,'retiro','transferencia'),(24,'2025-10-29 20:12:15.503554','pendiente_pago',8500.00,1,'delivery','transferencia');
/*!40000 ALTER TABLE `shop_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shop_orderitem`
--

DROP TABLE IF EXISTS `shop_orderitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shop_orderitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `cantidad` int NOT NULL,
  `precio_unitario` decimal(10,2) NOT NULL,
  `pedido_id` bigint NOT NULL,
  `producto_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `shop_orderitem_pedido_id_2afe1aa7_fk_shop_order_id` (`pedido_id`),
  KEY `shop_orderitem_producto_id_53046610_fk_shop_product_id` (`producto_id`),
  CONSTRAINT `shop_orderitem_pedido_id_2afe1aa7_fk_shop_order_id` FOREIGN KEY (`pedido_id`) REFERENCES `shop_order` (`id`),
  CONSTRAINT `shop_orderitem_producto_id_53046610_fk_shop_product_id` FOREIGN KEY (`producto_id`) REFERENCES `shop_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shop_orderitem`
--

LOCK TABLES `shop_orderitem` WRITE;
/*!40000 ALTER TABLE `shop_orderitem` DISABLE KEYS */;
INSERT INTO `shop_orderitem` VALUES (14,1,6400.00,13,4),(15,1,5600.00,14,2),(16,2,6600.00,14,5),(18,5,6500.00,16,1),(19,2,2200.00,17,23),(20,6,1200.00,17,17),(21,2,1800.00,18,25),(22,1,8500.00,18,9),(23,2,6400.00,19,3),(24,2,7500.00,19,20),(25,2,2200.00,19,23),(29,1,8500.00,23,9),(30,1,8500.00,24,9);
/*!40000 ALTER TABLE `shop_orderitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shop_product`
--

DROP TABLE IF EXISTS `shop_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shop_product` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `imagen` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `categoria_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `shop_product_categoria_id_7c34d3e4_fk_shop_category_id` (`categoria_id`),
  CONSTRAINT `shop_product_categoria_id_7c34d3e4_fk_shop_category_id` FOREIGN KEY (`categoria_id`) REFERENCES `shop_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shop_product`
--

LOCK TABLES `shop_product` WRITE;
/*!40000 ALTER TABLE `shop_product` DISABLE KEYS */;
INSERT INTO `shop_product` VALUES (1,'Cheese','Pan de papa, Medallon de carne, Cheddar, Mayonesa y Ketchup. Incluye papas fritas',6500.00,'productos/cheese.png',1),(2,'Cuarto de libra','Pan de Papa, Medallón de carne, Cheddar, Cebolla cruda, Mayonesa y Ketchup\r\nIncluye papas fritas',5600.00,'productos/cuarto.png',1),(3,'Bacon','Pan de papa, Medallon de carne, Cheddar, Panceta, Mayonesa y Ketchup\r\nIncluye papas fritas',6400.00,'productos/bacon.png',1),(4,'Clasica','Pan de papa, Medallon de carne, Cheddar, Lechuga, Tomate, Cebolla cruda, Huevo, Mayonesa y Ketchup\r\nIncluye papas fritas',6400.00,'productos/clasica.png',1),(5,'Tasty','Pan de papa, Medallon de carne, Cheddar, Lechuga, Tomate, Cebolla salteada, Bacon y Salsa ALIOLI\r\nIncluye papas fritas',6600.00,'productos/tasty.png',1),(6,'Mexa','Pan de papa, Medallon de carne, Queso tybo, Pimientos salteados, Cebolla Salteada y Salsa PICANTE',6000.00,'productos/mexa.png',1),(8,'Pepperoni','Salsa de tomate, mozzarella, pepperoni, aceite de oliva, especias',8000.00,'productos/caprese.jpg',2),(9,'Cuatro Quesos','Salsa de tomate, mozzarella, parmesano, provolone, roquefort, aceite de oliva, especias',8500.00,'productos/4quesos.jpg',2),(10,'Especial','Salsa de tomate, mozzarella, jamón, morrón, tomate, albahaca, aceite de oliva, especias.',7500.00,'productos/especial.jpg',2),(11,'Brocoli','Salsa de tomate, mozzarella, aceitunas negras, pimiento, brócoli, aceite de oliva, especias.',7500.00,'productos/brocoli.jpg',2),(12,'Bacon','Salsa de tomate, mozzarella, bacon, aceite de oliva, especias.',9000.00,'productos/bacon.jpg',2),(13,'Empanadas de Carne','Masa de empanada, carne picada, tomate, huevo, cebolla, aceite de oliva, sal',1100.00,'productos/empanadascarnepicada.png',8),(15,'Empanadas de Pollo','Masa de empanadas, pollo desmenuzado, queso, cebolla, sal',1100.00,'productos/empanadaspollo.png',8),(16,'Empanadas de JyQ','Masa de empanadas, jamón, queso mozzarella, cebolla, aceite de oliva, sal',1000.00,'productos/empanadasjyq2_POIXKeA.jpg',8),(17,'Empanadas Árabes','Masa empanada, cebolla, carne picada, morrón, tomate, jugo del limón, especias',1200.00,'productos/empanadasarabes.png',8),(18,'Papas Fritas','Papas fritas',6500.00,'productos/papasfritas.png',5),(19,'Papas Fritas con Cheddar y Bacon','Papas fritas bañadas en cheddar y con trocitos de Bacon.',8000.00,'productos/papasfritasconbacon.png',5),(20,'Papas Fritas con Huevo','Papas fritas a caballo, con cebolla de verdeo.',7500.00,'productos/papasfritasconhuevo.png',5),(21,'Sandwich Milanesa','Pan, milanesa frita, aderezos, lechuga, tomate, huevo, jamón y queso.',11000.00,'productos/sandwichmilanesa.png',4),(22,'Sandwich Lomito','Pan, lomito, lechuga, tomate, huevo, aderezos, jamón y queso',15000.00,'productos/sandwichlomito.png',4),(23,'Coca-Cola','Bebida Coca-Cola fresca 500ml',2200.00,'productos/cocacola.png',6),(24,'Agua Mineral','Agua mineral Villavicencio 500ml',1500.00,'productos/aguamineral.png',6),(25,'Agua Saborizada Manzana','Agua saborizada de manzana 500ml',1800.00,'productos/aguasaborizadamanzana_RcvbLPI.png',6),(26,'Agua Saborizada Pera','Agua saborizada de pera 500ml',1800.00,'productos/aguasaborizadapera.png',6),(27,'Postre Chocotorta','Galletas chocolinas, dulce de leche, queso mascarpone, café',2000.00,'productos/chocotorta.png',7),(28,'Postre Oreo','Galletas oreo, crema de leche, leche condensada, queso crema, esencia de vainilla',2100.00,'productos/oreo.png',7);
/*!40000 ALTER TABLE `shop_product` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-29 20:24:13
