-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 15, 2021 at 05:42 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library`
--

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `BookID` int(5) NOT NULL,
  `BookName` varchar(20) NOT NULL,
  `Shabak` int(10) NOT NULL,
  `Price` varchar(20) NOT NULL,
  `Subject` varchar(20) NOT NULL,
  `Count` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`BookID`, `BookName`, `Shabak`, `Price`, `Subject`, `Count`) VALUES
(1001, 'Binavayan', 1234, '100000', 'Novel', 5),
(1002, 'BoofKoor', 3453, '80000', 'Novel', 7),
(1003, 'DolatFarzanegi', 4527, '60000', 'Psycholofical', 2),
(1004, 'The Note Book', 4458, '120000', 'Love Story', 8),
(1005, 'Physics', 6732, '40000', 'Education', 2),
(1006, 'Little Prince ', 247545, '65000', 'Story', 6),
(1007, 'Shahnameh', 751208, '500000', 'Persian poem ', 3),
(1009, 'Golestan', 4532, '90000', 'Poem', 0);

-- --------------------------------------------------------

--
-- Table structure for table `borrowed`
--

CREATE TABLE `borrowed` (
  `BorrowID` int(5) NOT NULL,
  `MemberID` int(5) NOT NULL,
  `BookID` int(5) NOT NULL,
  `startDate` date NOT NULL DEFAULT current_timestamp(),
  `FinishDate` date NOT NULL DEFAULT current_timestamp(),
  `Situation` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `borrowed`
--

INSERT INTO `borrowed` (`BorrowID`, `MemberID`, `BookID`, `startDate`, `FinishDate`, `Situation`) VALUES
(1, 2005, 1007, '2021-12-15', '2021-12-15', 0),
(8, 2006, 1006, '2021-12-15', '2021-12-15', 0),
(9, 2002, 1005, '2021-12-15', '2021-12-15', 0);

-- --------------------------------------------------------

--
-- Table structure for table `members`
--

CREATE TABLE `members` (
  `MemberId` int(5) NOT NULL,
  `FirstName` varchar(20) NOT NULL,
  `LastName` varchar(20) NOT NULL,
  `National` int(10) NOT NULL,
  `phone` int(11) NOT NULL,
  `Username` varchar(50) NOT NULL,
  `PassWord` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `members`
--

INSERT INTO `members` (`MemberId`, `FirstName`, `LastName`, `National`, `phone`, `Username`, `PassWord`) VALUES
(2001, 'Mohammad', 'Alavi', 863429754, 912345678, 'Moh', '12345'),
(2002, 'Mahsa', 'Hoseini', 35648630, 912345634, 'mah', '12345'),
(2003, 'Ali', 'Rad', 35648630, 912655634, 'al', '6789'),
(2004, 'Fatemeh', 'Norouzi', 23567897, 912654334, 'fat', '12345'),
(2005, 'Hosein', 'Sadeghi', 125647, 9124587, 'hos', '6789'),
(2006, 'Dara', 'Shabani', 2356325, 991653782, 'zib', '12345');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`BookID`);

--
-- Indexes for table `borrowed`
--
ALTER TABLE `borrowed`
  ADD PRIMARY KEY (`BorrowID`);

--
-- Indexes for table `members`
--
ALTER TABLE `members`
  ADD PRIMARY KEY (`MemberId`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `books`
--
ALTER TABLE `books`
  MODIFY `BookID` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1010;

--
-- AUTO_INCREMENT for table `borrowed`
--
ALTER TABLE `borrowed`
  MODIFY `BorrowID` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `members`
--
ALTER TABLE `members`
  MODIFY `MemberId` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2009;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
