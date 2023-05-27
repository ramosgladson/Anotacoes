package com.educandoweb.course.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.educandoweb.course.entities.User;

public interface UserRepo extends JpaRepository<User, Long> {

}