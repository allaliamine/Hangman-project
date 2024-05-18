-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 18, 2024 at 10:48 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hangman`
--

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

CREATE TABLE `account` (
  `idaccount` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `account`
--

INSERT INTO `account` (`idaccount`, `username`, `password`) VALUES
(1, ' allali', 'allali123'),
(2, 'insaf ', 'insaf123');

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `idadmin` int(11) NOT NULL,
  `idaccount` int(11) NOT NULL,
  `name` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `hint`
--

CREATE TABLE `hint` (
  `idhint` int(11) NOT NULL,
  `idword` int(20) NOT NULL,
  `hintvalue` mediumtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `hint`
--

INSERT INTO `hint` (`idhint`, `idword`, `hintvalue`) VALUES
(1, 1, 'The largest land animal, known for its trunk and tusks.'),
(2, 3, ' An Australian marsupial that hops and has a pouch.'),
(3, 2, 'A flightless bird that swims, found in Antarctica.'),
(4, 4, 'A large aquatic reptile with a powerful jaw, found in rivers.'),
(5, 5, 'The tallest animal, known for its long neck and spots.'),
(6, 6, 'An egg-laying mammal with a duck bill, found in Australia.'),
(7, 7, 'A lizard known for changing its color.'),
(8, 15, 'an arab country  ,with a red flag'),
(9, 11, 'The country and continent known for the Outback and Sydney Opera House.'),
(10, 12, 'The largest country in South America, famous for the Amazon Rainforest and Carnival.'),
(11, 13, 'The second-largest country in the world, known for its maple syrup and hockey.'),
(12, 14, 'A country in North Africa known for its ancient pyramids and the Nile River.'),
(13, 23, 'A small, red fruit often used in pies and as a topping for desserts.'),
(14, 26, 'An exotic fruit with a vibrant pink skin and white flesh speckled with tiny seeds.'),
(15, 21, 'A common fruit that comes in red, green, or yellow varieties.'),
(16, 27, 'A small, green citrus fruit used to add flavor to food and drinks.'),
(17, 32, ' A sci-fi film set on the alien world of Pandora, directed by James Cameron.'),
(18, 39, 'A classic romance set during World War II, featuring the famous line \"Here\'s looking at you, kid.\"'),
(19, 38, 'A biographical drama about the life of composer Wolfgang Amadeus Mozart.');

-- --------------------------------------------------------

--
-- Table structure for table `history`
--

CREATE TABLE `history` (
  `idgame` int(11) NOT NULL,
  `iduser` int(20) NOT NULL,
  `idword` int(30) NOT NULL,
  `status` varchar(30) NOT NULL,
  `guessedletters` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `laderboard`
--

CREATE TABLE `laderboard` (
  `idladerboard` int(11) NOT NULL,
  `iduser` int(11) NOT NULL,
  `score` int(30) NOT NULL,
  `rank` int(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `player`
--

CREATE TABLE `player` (
  `iduser` int(11) NOT NULL,
  `idaccount` int(11) NOT NULL,
  `name` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `settings`
--

CREATE TABLE `settings` (
  `idsettings` int(11) NOT NULL,
  `iduser` int(11) NOT NULL,
  `hintenabled` varchar(30) NOT NULL,
  `theme` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `topic`
--

CREATE TABLE `topic` (
  `idtopic` int(11) NOT NULL,
  `topicname` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `topic`
--

INSERT INTO `topic` (`idtopic`, `topicname`) VALUES
(6, 'Animals'),
(7, 'Sports'),
(8, 'movies'),
(9, 'fruits'),
(10, 'books'),
(11, 'planets'),
(12, 'music'),
(13, 'colors'),
(14, 'Countries'),
(15, 'technology');

-- --------------------------------------------------------

--
-- Table structure for table `word`
--

CREATE TABLE `word` (
  `idword` int(11) NOT NULL,
  `idtopic` int(11) NOT NULL,
  `word` varchar(30) NOT NULL,
  `description` mediumtext NOT NULL,
  `difficulty-level` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `word`
--

INSERT INTO `word` (`idword`, `idtopic`, `word`, `description`, `difficulty-level`) VALUES
(1, 6, 'Elephant', '', 1),
(2, 6, 'penguin', '', 3),
(3, 6, 'kangaroo', '', 3),
(4, 6, 'crocodile', '', 2),
(5, 6, 'giraffe', '', 1),
(6, 6, 'platypus', '', 3),
(7, 6, 'chameleon', '', 2),
(8, 6, 'cat', '', 1),
(9, 6, 'hippopotamus', '', 3),
(10, 6, 'Orangutan', '', 3),
(11, 14, 'australia', '', 1),
(12, 14, 'brazil', '', 1),
(13, 14, 'canada', '', 2),
(14, 14, 'egypt', '', 2),
(15, 14, 'morocco', '', 3),
(16, 14, 'honduras', '', 3),
(17, 14, 'japan', '', 2),
(18, 14, 'finland', '', 3),
(19, 14, 'indounisia', '', 3),
(20, 14, 'saoudia', '', 3),
(21, 9, 'apple', '', 1),
(22, 9, 'banana', '', 1),
(23, 9, 'cherry', '', 2),
(24, 9, 'fig', '', 3),
(25, 9, 'kiwi', '', 2),
(26, 9, 'dragonfruit', '', 3),
(27, 9, 'lime', '', 3),
(28, 9, 'huckleberry', '', 3),
(29, 9, 'orange', '', 2),
(30, 8, 'inception', '', 1),
(31, 8, 'titanic', '', 1),
(32, 8, 'avatar', '', 2),
(33, 8, 'amadeus', '', 3),
(34, 8, 'casablanca', '', 0),
(35, 8, 'inception', '', 1),
(36, 8, 'titanic', '', 1),
(37, 8, 'avatar', '', 2),
(38, 8, 'amadeus', '', 3),
(39, 8, 'casablanca', '', 3),
(40, 11, 'venus', '', 1),
(41, 11, 'mars', '', 2),
(42, 11, 'pluto', '', 3),
(43, 11, 'saturn', '', 3),
(44, 7, 'soccer', '', 2),
(45, 7, 'badminton', '', 3),
(46, 7, 'archery', '', 3),
(47, 7, 'surfing', '', 2),
(48, 7, 'tennis', '', 1),
(49, 10, 'Moby Dick', '', 1),
(50, 10, 'hamlet', '', 1),
(51, 10, 'odyssey', '', 3),
(52, 10, 'inferno', '', 2),
(53, 10, 'iliad', '', 0),
(54, 10, 'Moby Dick', '', 1),
(55, 10, 'hamlet', '', 1),
(56, 10, 'odyssey', '', 3),
(57, 10, 'inferno', '', 2),
(58, 10, 'iliad', '', 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account`
--
ALTER TABLE `account`
  ADD PRIMARY KEY (`idaccount`);

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`idadmin`),
  ADD KEY `fk_account2` (`idaccount`);

--
-- Indexes for table `hint`
--
ALTER TABLE `hint`
  ADD PRIMARY KEY (`idhint`),
  ADD KEY `fk_word` (`idword`);

--
-- Indexes for table `history`
--
ALTER TABLE `history`
  ADD PRIMARY KEY (`idgame`),
  ADD KEY `fk_user` (`iduser`),
  ADD KEY `fk_word2` (`idword`);

--
-- Indexes for table `laderboard`
--
ALTER TABLE `laderboard`
  ADD PRIMARY KEY (`idladerboard`),
  ADD KEY `fk_user3` (`iduser`);

--
-- Indexes for table `player`
--
ALTER TABLE `player`
  ADD PRIMARY KEY (`iduser`),
  ADD KEY `fk_account1` (`idaccount`);

--
-- Indexes for table `settings`
--
ALTER TABLE `settings`
  ADD PRIMARY KEY (`idsettings`),
  ADD KEY `fk_user4` (`iduser`);

--
-- Indexes for table `topic`
--
ALTER TABLE `topic`
  ADD PRIMARY KEY (`idtopic`);

--
-- Indexes for table `word`
--
ALTER TABLE `word`
  ADD PRIMARY KEY (`idword`),
  ADD KEY `fk_topic` (`idtopic`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `account`
--
ALTER TABLE `account`
  MODIFY `idaccount` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `idadmin` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `hint`
--
ALTER TABLE `hint`
  MODIFY `idhint` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `history`
--
ALTER TABLE `history`
  MODIFY `idgame` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `laderboard`
--
ALTER TABLE `laderboard`
  MODIFY `idladerboard` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `player`
--
ALTER TABLE `player`
  MODIFY `iduser` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `settings`
--
ALTER TABLE `settings`
  MODIFY `idsettings` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `topic`
--
ALTER TABLE `topic`
  MODIFY `idtopic` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `word`
--
ALTER TABLE `word`
  MODIFY `idword` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=59;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `admin`
--
ALTER TABLE `admin`
  ADD CONSTRAINT `fk_account2` FOREIGN KEY (`idaccount`) REFERENCES `account` (`idaccount`);

--
-- Constraints for table `hint`
--
ALTER TABLE `hint`
  ADD CONSTRAINT `fk_word` FOREIGN KEY (`idword`) REFERENCES `word` (`idword`);

--
-- Constraints for table `history`
--
ALTER TABLE `history`
  ADD CONSTRAINT `fk_user` FOREIGN KEY (`iduser`) REFERENCES `player` (`iduser`),
  ADD CONSTRAINT `fk_word2` FOREIGN KEY (`idword`) REFERENCES `word` (`idword`);

--
-- Constraints for table `laderboard`
--
ALTER TABLE `laderboard`
  ADD CONSTRAINT `fk_user3` FOREIGN KEY (`iduser`) REFERENCES `player` (`iduser`);

--
-- Constraints for table `player`
--
ALTER TABLE `player`
  ADD CONSTRAINT `fk_account1` FOREIGN KEY (`idaccount`) REFERENCES `player` (`iduser`);

--
-- Constraints for table `settings`
--
ALTER TABLE `settings`
  ADD CONSTRAINT `fk_user4` FOREIGN KEY (`iduser`) REFERENCES `player` (`iduser`);

--
-- Constraints for table `word`
--
ALTER TABLE `word`
  ADD CONSTRAINT `fk_topic` FOREIGN KEY (`idtopic`) REFERENCES `topic` (`idtopic`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
