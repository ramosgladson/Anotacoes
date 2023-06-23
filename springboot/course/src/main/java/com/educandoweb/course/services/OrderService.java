package com.educandoweb.course.services;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.educandoweb.course.entities.Order;
import com.educandoweb.course.repository.OrderRepository;

@Service
public class OrderService {
    @Autowired
    private OrderRepository orderRepository;

    public List<Order> listAllOrders() {
        return orderRepository.findAll();
    }

    public Optional<Order> listById(Long id) {
        return orderRepository.findById(id);
    }

    public Order addOrder(Order order) {
        return orderRepository.save(order);
    }

}