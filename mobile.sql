-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 22, 2022 at 03:45 PM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mobile`
--

-- --------------------------------------------------------

--
-- Table structure for table `management`
--

CREATE TABLE `management` (
  `id` int(11) NOT NULL,
  `brand_name` varchar(50) DEFAULT NULL,
  `model` varchar(50) NOT NULL,
  `old_price` float DEFAULT NULL,
  `new_price` float DEFAULT NULL,
  `sales_2019` float DEFAULT NULL,
  `sales_2020` float DEFAULT NULL,
  `revenue` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `management`
--

INSERT INTO `management` (`id`, `brand_name`, `model`, `old_price`, `new_price`, `sales_2019`, `sales_2020`, `revenue`) VALUES
(1, 'Apple', 'iphoneX', 34900, 30000, 95421.7, 120442, 13755.8),
(2, 'Samsung', 'Galaxy S20', 24000, 29490, 74026.2, 77117.4, 78651),
(3, 'Xiaomi', 'MI Note4', 16999, 13590, 29187.8, 43430.3, 38196),
(4, 'Vivo', 'Vivo S1', 19890, 15900, 49803, 31315.7, 25060),
(5, 'Oppo', 'Oppo A5', 11490, 12999, 28704, 44373.7, 38757),
(6, 'Nokia', 'Nokia C30', 12900, 10999, 79038, 59924, 10206.7),
(7, 'Sony', 'Sony Xperia', 14000, 12999, 70206, 62789.8, 57216);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `management`
--
ALTER TABLE `management`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `management`
--
ALTER TABLE `management`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
