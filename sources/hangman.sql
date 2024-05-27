-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost
-- Généré le : lun. 27 mai 2024 à 13:46
-- Version du serveur : 10.4.28-MariaDB
-- Version de PHP : 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `hangman`
--

-- --------------------------------------------------------

--
-- Structure de la table `account`
--

CREATE TABLE `account` (
  `idaccount` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(30) NOT NULL,
  `name` varchar(30) NOT NULL,
  `role` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `account`
--

INSERT INTO `account` (`idaccount`, `username`, `password`, `name`, `role`) VALUES
(1, 'allali', 'allali123', 'amine', 0),
(15, 'ilias123', '1234', 'ilias', 1),
(16, 'allali99', '123', 'amine', 1),
(17, 'insaf', 'insaf123', 'insaf', 1);

-- --------------------------------------------------------

--
-- Structure de la table `hint`
--

CREATE TABLE `hint` (
  `idhint` int(11) NOT NULL,
  `idword` int(20) NOT NULL,
  `hintvalue` mediumtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `hint`
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
(18, 39, 'A classic romance set during World War II'),
(19, 38, 'A biographical drama about the life of composer Wolfgang Amadeus Mozart.'),
(20, 8, 'furry creature often kept as a pet and known for its independent nature.'),
(21, 9, 'a large, herbivorous mammal known for its massive size and amphibious habits.'),
(22, 10, 'a reddish-brown primate native to the rainforests of Borneo and Sumatra, known for its long arms and tree-dwelling lifestyle.'),
(23, 16, 'a country in Central America known for its Caribbean Sea coastline and Mayan ruins.\r\n\r\n\r\n\r\n\r\n\r\n\r\n'),
(24, 17, 'an island nation in East Asia known for its technology, sushi, and rich cultural heritage.'),
(25, 18, 'Nordic country in Northern Europe known for its lakes, forests, and Northern Lights.'),
(26, 19, 'Southeast Asian country made up of thousands of islands, known for its beaches, volcanoes, and diverse cultures.'),
(27, 20, 'Middle Eastern country known for its vast deserts, oil wealth, and the cities of Mecca and Medina.');

-- --------------------------------------------------------

--
-- Structure de la table `laderboard`
--

CREATE TABLE `laderboard` (
  `idladerboard` int(11) NOT NULL,
  `idaccount` int(11) NOT NULL,
  `score` int(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `laderboard`
--

INSERT INTO `laderboard` (`idladerboard`, `idaccount`, `score`) VALUES
(1, 1, 11),
(2, 10, 1),
(3, 17, 1);

-- --------------------------------------------------------

--
-- Structure de la table `settings`
--

CREATE TABLE `settings` (
  `idsettings` int(11) NOT NULL,
  `idaccount` int(11) NOT NULL,
  `hintenabled` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `settings`
--

INSERT INTO `settings` (`idsettings`, `idaccount`, `hintenabled`) VALUES
(1, 1, 0),
(2, 15, 1),
(3, 16, 1),
(4, 17, 0);

-- --------------------------------------------------------

--
-- Structure de la table `topic`
--

CREATE TABLE `topic` (
  `idtopic` int(11) NOT NULL,
  `topicname` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `topic`
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
-- Structure de la table `word`
--

CREATE TABLE `word` (
  `idword` int(11) NOT NULL,
  `idtopic` int(11) NOT NULL,
  `word` varchar(30) NOT NULL,
  `difficulty` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `word`
--

INSERT INTO `word` (`idword`, `idtopic`, `word`, `difficulty`) VALUES
(1, 6, 'Elephant', 0),
(2, 6, 'penguin', 2),
(3, 6, 'kangaroo', 2),
(4, 6, 'crocodile', 1),
(5, 6, 'giraffe', 0),
(6, 6, 'platypus', 2),
(7, 6, 'chameleon', 1),
(8, 6, 'cat', 0),
(9, 6, 'hippopotamus', 2),
(10, 6, 'Orangutan', 2),
(11, 14, 'australia', 0),
(12, 14, 'brazil', 0),
(13, 14, 'canada', 1),
(14, 14, 'egypt', 1),
(15, 14, 'morocco', 2),
(16, 14, 'honduras', 2),
(17, 14, 'japan', 1),
(18, 14, 'finland', 2),
(19, 14, 'indounisia', 2),
(20, 14, 'saoudia', 2),
(21, 9, 'apple', 0),
(22, 9, 'banana', 0),
(23, 9, 'cherry', 1),
(24, 9, 'fig', 2),
(25, 9, 'kiwi', 1),
(26, 9, 'dragonfruit', 2),
(27, 9, 'lime', 2),
(28, 9, 'huckleberry', 2),
(29, 9, 'orange', 1),
(30, 8, 'inception', 0),
(31, 8, 'titanic', 0),
(32, 8, 'avatar', 1),
(33, 8, 'amadeus', 2),
(34, 8, 'casablanca', 1),
(35, 8, 'inception', 0),
(36, 8, 'titanic', 0),
(37, 8, 'avatar', 1),
(38, 8, 'amadeus', 2),
(39, 8, 'casablanca', 2),
(40, 11, 'venus', 0),
(41, 11, 'mars', 1),
(42, 11, 'pluto', 2),
(43, 11, 'saturn', 2),
(44, 7, 'soccer', 1),
(45, 7, 'badminton', 2),
(46, 7, 'archery', 2),
(47, 7, 'surfing', 1),
(48, 7, 'tennis', 0),
(49, 10, 'Moby Dick', 0),
(50, 10, 'hamlet', 0),
(51, 10, 'odyssey', 2),
(52, 10, 'inferno', 1),
(53, 10, 'iliad', 0),
(54, 10, 'Moby Dick', 0),
(55, 10, 'hamlet', 0),
(56, 10, 'odyssey', 2),
(57, 10, 'inferno', 1),
(58, 10, 'iliad', 1);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `account`
--
ALTER TABLE `account`
  ADD PRIMARY KEY (`idaccount`);

--
-- Index pour la table `hint`
--
ALTER TABLE `hint`
  ADD PRIMARY KEY (`idhint`),
  ADD KEY `fk_word` (`idword`);

--
-- Index pour la table `laderboard`
--
ALTER TABLE `laderboard`
  ADD PRIMARY KEY (`idladerboard`),
  ADD KEY `fk_account_laderboard` (`idaccount`);

--
-- Index pour la table `settings`
--
ALTER TABLE `settings`
  ADD PRIMARY KEY (`idsettings`),
  ADD KEY `fk1_account` (`idaccount`);

--
-- Index pour la table `topic`
--
ALTER TABLE `topic`
  ADD PRIMARY KEY (`idtopic`);

--
-- Index pour la table `word`
--
ALTER TABLE `word`
  ADD PRIMARY KEY (`idword`),
  ADD KEY `fk_topic` (`idtopic`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `account`
--
ALTER TABLE `account`
  MODIFY `idaccount` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT pour la table `hint`
--
ALTER TABLE `hint`
  MODIFY `idhint` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT pour la table `laderboard`
--
ALTER TABLE `laderboard`
  MODIFY `idladerboard` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT pour la table `settings`
--
ALTER TABLE `settings`
  MODIFY `idsettings` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `topic`
--
ALTER TABLE `topic`
  MODIFY `idtopic` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT pour la table `word`
--
ALTER TABLE `word`
  MODIFY `idword` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=59;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `hint`
--
ALTER TABLE `hint`
  ADD CONSTRAINT `fk_word` FOREIGN KEY (`idword`) REFERENCES `word` (`idword`);

--
-- Contraintes pour la table `laderboard`
--
ALTER TABLE `laderboard`
  ADD CONSTRAINT `fk_account_laderboard` FOREIGN KEY (`idaccount`) REFERENCES `account` (`idaccount`);

--
-- Contraintes pour la table `settings`
--
ALTER TABLE `settings`
  ADD CONSTRAINT `fk1_account` FOREIGN KEY (`idaccount`) REFERENCES `account` (`idaccount`);

--
-- Contraintes pour la table `word`
--
ALTER TABLE `word`
  ADD CONSTRAINT `fk_topic` FOREIGN KEY (`idtopic`) REFERENCES `topic` (`idtopic`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
