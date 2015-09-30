-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema givr
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema givr
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `givr` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `givr` ;

-- -----------------------------------------------------
-- Table `givr`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `givr`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT COMMENT '',
  `first_name` VARCHAR(45) NULL COMMENT '',
  `last_name` VARCHAR(45) NULL COMMENT '',
  `email` VARCHAR(45) NULL COMMENT '',
  `username` VARCHAR(45) NULL COMMENT '',
  `created_at` DATETIME NULL COMMENT '',
  `password` VARCHAR(300) NULL COMMENT '',
  `user_img` VARCHAR(45) NULL COMMENT '',
  `description` TEXT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '')
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `givr`.`reports`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `givr`.`reports` (
  `id` INT NOT NULL AUTO_INCREMENT COMMENT '',
  `dates` DATETIME NULL COMMENT '',
  `description` VARCHAR(45) NULL COMMENT '',
  `location` VARCHAR(45) NULL COMMENT '',
  `lat` FLOAT NULL COMMENT '',
  `long` FLOAT NULL COMMENT '',
  `created_at` DATETIME NULL COMMENT '',
  `modified_at` DATETIME NULL COMMENT '',
  `users_id` INT NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  INDEX `fk_reports_users1_idx` (`users_id` ASC)  COMMENT '',
  CONSTRAINT `fk_reports_users1`
    FOREIGN KEY (`users_id`)
    REFERENCES `givr`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `givr`.`helpee`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `givr`.`helpee` (
  `id` INT NOT NULL AUTO_INCREMENT COMMENT '',
  `helpee_img` VARCHAR(45) NULL COMMENT '',
  `created_at` DATETIME NULL COMMENT '',
  `updated_at` DATETIME NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '')
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `givr`.`request`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `givr`.`request` (
  `id` INT NOT NULL AUTO_INCREMENT COMMENT '',
  `description` VARCHAR(45) NULL COMMENT '',
  `comments` VARCHAR(200) NULL COMMENT '',
  `location` VARCHAR(45) NULL COMMENT '',
  `lat` FLOAT NULL COMMENT '',
  `long` FLOAT NULL COMMENT '',
  `image_address` VARCHAR(200) NULL COMMENT '',
  `created_at` DATETIME NULL COMMENT '',
  `updated_at` DATETIME NULL COMMENT '',
  `users_id` INT NOT NULL COMMENT '',
  `helpee_id` INT NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  INDEX `fk_request_users_idx` (`users_id` ASC)  COMMENT '',
  INDEX `fk_request_helpee1_idx` (`helpee_id` ASC)  COMMENT '',
  CONSTRAINT `fk_request_users`
    FOREIGN KEY (`users_id`)
    REFERENCES `givr`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_request_helpee1`
    FOREIGN KEY (`helpee_id`)
    REFERENCES `givr`.`helpee` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
